# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

import settings
import board


class GameController():
    """
      Interact with real game on website slowotok.pl
      To interact with game Selenium is used.
    """

    def __init__(self, login, password):
        self.login = login
        self.password = password

        self.set_driver()

        if not settings.DEBUG:
            self.login()
            self.go_to_game()

        self.start_game()

    def set_driver(self):
        self.d = webdriver.Firefox()
        if settings.DEBUG:
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

        i = 0
        while i < 10:
            i += 1
            if self.can_play():
                print "Can play!"
                self.load_board()
                break
            else:
                print "have to wait..."
                self.wait_for_status_change()

    def can_play(self):
        status_info = self.d.find_element_by_id("time_desc").text
        time_text = self.d.find_element_by_id("time").text
        minutes, seconds = time_text.split(":")
        if not status_info.startswith("DO KO"):
            print "status nie do konca"
            return False
        elif int(minutes) == 0:
            print "wait seconds", seconds
            time.sleep(int(seconds))
            return False
        else:
            print "kosmaty"
            return True

    def get_game_elements(self):
        self.clock = self.d.find_element_by_id("time")

    def wait_for_status_change(self):
        wait = WebDriverWait(self.d, 180)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'time_desc'),
                                                    u"DO KOŃCA"))
        print "end wait until"

    def load_board(self):
        self.board = board.Board()
        for block in self.d.find_elements_by_css_selector("#board>.block"):
            letter = block.get_attribute('letter')
            block_id = block.get_attribute('id')
            self.board.add_block(letter, block_id)

        self.board.set_blocks_neighbous()
