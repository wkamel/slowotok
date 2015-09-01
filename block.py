# -*- coding: utf-8 -*-

BOARD_SIZE = 4  # TODO move to some settings file


class Block():
    """
        Represents single element on board:
        it have it's column, row, id and letter name
    """

    def __init__(self, letter, block_id):
        self.__letter = unicode(letter.lower()).encode('utf-8')
        self.__id = int(block_id)
        self.__row = int(self.__id / BOARD_SIZE)
        self.__column = int(self.__id % BOARD_SIZE)

    def get_id(self):
        return self.__id

    def get_letter(self):
        return self.__letter

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__column

    def __str__(self):
        return unicode("[%s][%s] %s: %s" % (self.__row,
                                            self.__column,
                                            self.__letter,
                                            self.__id)
                       ).encode('utf-8')
