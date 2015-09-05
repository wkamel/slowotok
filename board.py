# -*- coding: utf-8 -*-
from block import Block
import settings


class Board():
    """
      Represents board - table of letters(blocks)
    """
    _blocks = set()

    def add_block(self, letter, block_id):
        block = Block(letter, block_id)
        row, col = block.get_position()
        self._blocks.add(block)

    def set_blocks_neighbours(self):
        for block in self._blocks:
            self.set_one_block_neighbours(block)

            # block.add_neighbour(block)

    def set_one_block_neighbours(self, block):
        b_row = block.row
        b_col = block.column

        for row in [-1, 0, 1]:
            sib_row = b_row + row
            for col in [-1, 0, 1]:
                sib_col = b_col + col
                if self.valid_indexes(sib_row, sib_col):
                    block.add_neighbour(self.get_block(sib_row, sib_col))

    def valid_indexes(self, row, col):
        return (row < self.get_size()
                and row >= 0
                and col < self.get_size()
                and col >= 0)

    def get_blocks(self):
        for l in self._blocks:
            yield l

    def get_block(self, row, col):
        for b in self._blocks:
            if b.row  == row and b.column == col:
                return b

    def show(self):
        return True

    @staticmethod
    def get_size():
        return settings.BOARD_SIZE
