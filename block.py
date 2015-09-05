# -*- coding: utf-8 -*-

import settings


class Block():
    """
        Represents single element on board:
        it have it's column, row, id and letter name
    """

    def __init__(self, letter, block_id):
        self.neighbours = set()
        self.letter = unicode(letter.lower()).encode('utf-8')
        self.id = int(block_id)
        self.row = int((self.id-1) / settings.BOARD_SIZE)
        self.column = int((self.id-1) % settings.BOARD_SIZE)
        if self.column == -1:
            self.column = settings.BOARD_SIZE-1

    def add_neighbour(self, block):
        if block is not self:
            self.neighbours.add(block)

    # def get_neighbours(self):
    #    return self.neigbours

    def get_neighbours_ids(self):
        return self.neigbours_ids

    def get_neighbours_amount(self):
        return len(self.neigbours)

    def get_position(self):
        return self.row, self.column

    def get_row(self):
        return self.row

    def get_col(self):
        return self.column

    def __str__(self):
        return ("[%s][%s] %s: %s" % (self.row,
                                     self.column,
                                     self.__letter,
                                     self.id)
                )
