# -*- coding: utf-8 -*-
from block import Block

BOARD_SIZE = 4


class Board():
    """
      Represents board - table of letters(blocks)
    """
    __blocks = []

    def add_block(self, letter, block_id):
        self.__blocks.append(Block(letter, block_id))

    def get_blocks(self):
        for l in self.__blocks:
            yield l

    def get_block(self, row, col):
        for b in self.__blocks:
            if b.get_row() == row and b.get_col() == col:
                return b

        return False

    def show(self):
        return True

    @staticmethod
    def get_size():
        return BOARD_SIZE
