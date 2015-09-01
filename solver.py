# -*- coding: utf-8 -*-
#
# TODO - prove of concept
#  demands many perfomance improvements
#  in:
#  - finding siblings
#  - searching in dictionary
#


class LetterWords():
    """
     Builds letter combinations(potencially words)
     from letters which are neighbours -
     lays in distance of one position in any direction.
    """
    words = []

    def __init__(self, board, block):
        self.used_blocks = []
        self.board = board
        self.add_block(block, "", [])

    # @profile
    def add_block(self, block, word, used_blocks):
        used_blocks.append(block)
        word += block.get_letter()
        if len(word) > 2:
            if word not in self.words:
                self.words.append(word)

        self.get_neighbours(block, word, used_blocks)

    # @profile # TODO - too slow
    def get_neighbours(self, block, word, used_blocks):
        """
        """
        b_row = block.get_row()
        b_col = block.get_col()

        for row in [-1, 0, 1]:
            for col in [-1, 0, 1]:
                sib_row = b_row + row
                sib_col = b_col + col
                if (sib_row < self.board.get_size()
                   and sib_row >= 0
                   and sib_col < self.board.get_size()
                   and sib_col >= 0):

                    block = self.board.get_block(sib_row, sib_col)
                    ub = used_blocks[:]
                    if block not in used_blocks and len(used_blocks) < 5:
                        # print "[%d][%d]= %s, len:%d" % (block.get_row(),
                        #                           block.get_col(),
                        #                           block.get_letter(),
                        #                           len(used_blocks)
                        #                           )
                        self.add_block(block, word, ub)


class Solver():
    """
      Class to find if letters combinations
      are real words - compare them with dictionary
    """
    words = []
    dictionary = []

    def __init__(self, board):
        self.__board = board
        self.load_dictionary()

    # @profile
    def solve(self):
        for letter in self.__board.get_blocks():
            LetterWords(self.__board, letter)

        for w in LetterWords.words:
            if w in self.dictionary:
                print "new word:", w
                self.words.append(w)

    def load_dictionary(self):
        with open('nouns.txt') as f:
            for line in f.readlines():
                self.dictionary.append(line[:-2])
