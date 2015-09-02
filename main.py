# -*- coding: utf-8 -*-


"""
    Slowotok solver.
    Module for finding words in board of letters.
    Automatically logs in into slowotok web aplication using Selenium,
    to read letters to solve.
    Waits for next game if current game ends.

"""


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import argparse
import board
from solver import Solver


class Slowotok():
    app_login_url = "http://slowotok.pl/account/logon"
    debug_url = "http://localhost/testslow/index.html"

    def __init__(self, login, password, debug=False):
        self.login = login
        self.password = password
        self.debug = debug
        self.set_driver()
        if not self.debug:
            self.login()
            self.go_to_game()

        self.start_game()

    def set_driver(self):
        self.d = webdriver.Firefox()
        if self.debug:
            self.d.get(self.debug_url)
        else:
            self.d.get(self.app_login_url)

    def login(self):
        email = self.d.find_element_by_name("Email")
        password = self.d.find_element_by_name("Password")
        submit = self.d.find_element_by_xpath("//input[@type='submit']")
        email.send_keys(self.login)
        password.send_keys(self.password)
        submit.click()

    def go_to_game(self):
        join_game_btn = self.d.find_element_by_xpath("//a[@href='/play']")
        join_game_btn.click()

    def start_game(self):
        self.get_game_elements()

        i = 3
        while i < 10:
            i += 1
            if self.can_play():
                print "Can play!"
                self.play()
                break
            else:
                print "have to wait..."
                self.wait_for_status_change()

    def can_play(self):
        status_info = self.d.find_element_by_id("time_desc").text
        time_text = self.d.find_element_by_id("time").text
        minutes, seconds = time_text.split(":")
        if not status_info.startswith("DO KO"):
            return False
        elif int(minutes) == 0:
            print "wait seconds", seconds
            time.sleep(int(seconds))
            return False
        else:
            return True

    def get_game_elements(self):
        self.clock = self.d.find_element_by_id("time")

    def wait_for_status_change(self):
        wait = WebDriverWait(self.d, 180)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'time_desc'),
                                                    u"DO KOŃCA"))
        print "end wait until"

    def play(self):
        self.get_board()
        # self.board.show()
        solver = Solver(self.board)
        solver.solve()

    def get_board(self):
        self.board = board.Board()
        for block in self.d.find_elements_by_css_selector("#board>.block"):
            letter = block.get_attribute('letter')
            block_id = block.get_attribute('id')
            self.board.add_block(letter, block_id)


if __name__ == '__main__':
    debug = True  # TODO - move to settings file

    parser = argparse.ArgumentParser(description="""Slowotok solver needs
                                     your Slowotok login data""")
    parser.add_argument('-login', required=True,
                        help='Your login in Slowotok')
    parser.add_argument('-password', required=True,
                        help='Your password in Slowotok')

    args = parser.parse_args()
    if not args.login or not args.password:
        print parser.print_help()
    else:
        Slowotok(args.login, args.password, debug)
