# -*- coding: utf-8 -*-
from solver import Solver
from board import Board

letters = ['ć', 'o', 'y', 's',
           'a', 'w', 'b', 't',
           'i', 'e', 'i', 'u',
           'g', 'r', 'h', 'k'
           ]

xletters = ['a', 'b',
           't', 'o', ]


board = Board()
for no, letter in enumerate(letters):
    block_id = no + 1
    letter = letter.decode('utf-8')
    board.add_block(letter, block_id)

board.set_blocks_neighbours()

# self.board.show()
solver = Solver(board)
solver.solve()
