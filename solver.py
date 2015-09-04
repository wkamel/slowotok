# -*- coding: utf-8 -*-
#
# TODO - prove of concept
#  it demands many perfomance improvements
#  in:
#  - finding siblings
#  - searching in dictionary
#


class LetterCombinations():
    """
     Builds letter combinations(potencially combinations)
     from letters which are neighbours -
     lays in distance of one position in any direction.
    """
    board = None
    combinations = []

    def __init__(self, block):
        self.used_blocks = []
        self.add_block(block, "", [])

    @profile
    def add_block(self, block, word, used_blocks):
        used_blocks.append(block)
        word += block.get_letter()
        if len(word) > 2:
            self.combinations.append(word)

        self.get_neighbours(block, word, used_blocks)

    @profile  # TODO - too slow
    def get_neighbours(self, block, word, used_blocks):
        """
        """
        ub = used_blocks[:]
        [self.add_block(neighbour, word, ub)
         for neighbour in block.get_neighbours() if neighbour not in used_blocks]
        # for neighbour in block.get_neighbours():
        #    if neighbour not in used_blocks:
        #        self.add_block(neighbour, word, ub)


class Solver():
    """
      Class to find if letters combinations
      are real combinations - compare them with dictionary
    """
    combinations = []
    dictionary = {}

    def __init__(self, board):
        self._board = board
        self.load_dictionary()

    @profile
    def solve(self):
        LetterCombinations.board = self._board
        combinations = self.create_letters_combinations()
        sorted(combinations)
        # words = [combination for combination in self.combinations if combination in self.dictionary]
        self.find_combinations(combinations)



    @profile
    def load_dictionary(self):
        words = {}
        with open('nouns.txt') as f:
            map(self.create_key_and_append_word, f.readlines())

        return True

        for w in words:
            first_letter = w[0]
            if first_letter not in self.dictionary:
                   self.dictionary[first_letter] = []

            self.dictionary[w[0]].append(w)

    def create_key_and_append_word(self, line):
        first_letter, word = line[0], line[:-2]
        if first_letter not in self.dictionary:
            self.dictionary[first_letter] = []

        self.dictionary[first_letter].append(word)


    def create_letters_combinations(self):
        map(LetterCombinations, self._board.get_blocks())
        return set(LetterCombinations.combinations)

    @profile
    def find_combinations(self, combinations):
        map(self.check_combination, combinations)
        # for combination in combinations:
        #     first_letter = combination[0]
        #     if combination in self.dictionary[first_letter]:
        #         print "jest", combination

    def check_combination(self, combination):
        first_letter = combination[0]
        if combination in self.dictionary[first_letter]:
            print "jest", combination

