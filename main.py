# -*- coding: utf-8 -*-


"""
    Slovotok solver.
    Module for finding words in board of letters.
    Automatically logs in into slowotok web aplication using Selenium,
    to read letters to solve.
    Waits for next game if current game ends.

"""

import argparse
from solver import Solver
from game_controller import GameController


class Slowotok():
    """
        Main program module
    """
    def play(self, login, password):
        game_controller = GameController()
        game_controller.load_board()
        board = self.get_board()
        # self.board.show()
        solver = Solver(board)
        solver.solve()


if __name__ == '__main__':

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
        slowotok = Slowotok()
        slowotok.play(args.login, args.password)
