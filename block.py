# -*- coding: utf-8 -*-

import settings


class Block():
    """
        Represents single element on board:
        it have it's column, row, id and letter name
    """

    def __init__(self, letter, block_id):
        self.neigbours = []
        self.__letter = unicode(letter.lower()).encode('utf-8')
        self.__id = int(block_id)
        self.__row = int((self.__id-1) / settings.BOARD_SIZE)
        self.__column = int((self.__id-1) % settings.BOARD_SIZE)
        if self.__column == -1:
            self.__column = settings.BOARD_SIZE-1

    def add_neighbour(self, block):
        if block is not self:
            self.neigbours.append(block)

    def get_neighbours(self):
        return self.neigbours

    def get_neighbours_amount(self):
        return len(self.neigbours)

    def get_id(self):
        return self.__id

    def get_letter(self):
        return self.__letter

    def get_position(self):
        return self.get_row(), self.get_col()

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__column

    def __str__(self):
        return ("[%s][%s] %s: %s" % (self.__row,
                                     self.__column,
                                     self.__letter,
                                     self.__id)
                )
