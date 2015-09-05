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
    combinations = set()

    def __init__(self, block):
        # k = []
        self.add_block(block, "", set())

    @profile
    def add_block(self, block, word, used_blocks):
        used_blocks.add(block.id)
        # blocks_str = ", ".join(map(lambda b: b.get_letter(), used_blocks))
        # taby = " " * len(used_blocks)
        # word += block.letter
        # self.combinations.add(word)
        self.add_neighbours(block, word, used_blocks)

    @profile  # TODO - too slow
    def add_neighbours(self, block, word, used_blocks):
        if len(used_blocks) < 9:
            for neighbour in block.neighbours:
                if neighbour.id not in used_blocks:
                    # neighbours = map(lambda n: n.get_letter(),  block.get_neighbours())
                    # print block.get_letter()
                    # print ",".join(neighbours)
                    self.add_block(neighbour, word, set(used_blocks))

        # [self.add_block(neighbour, word, used_blocks[:])
        #  for neighbour in block.get_neighbours() if neighbour not in used_blocks]


class Solver():
    """
      Class to find if letters combinations
      are real combinations - compare them with dictionary
    """
    _dictionary = {}
    _words = []

    def __init__(self, board):
        self._board = board
        self.load_dictionary()

    @profile
    def solve(self):
        LetterCombinations.board = self._board
        combinations = self.create_letters_combinations()

        self.find_combinations(combinations)

    def load_dictionary(self):
        with open('nouns.txt') as f:
            self._dictionary = set([x[:-2] for x in f.readlines()])

    # @profile
    def create_letters_combinations(self):
        map(LetterCombinations, self._board.get_blocks())
        # LetterCombinations(self._board.get_block(0, 1))
        return set(LetterCombinations.combinations)

    def find_combinations(self, combinations):
        for combination in combinations:
            if combination in self._dictionary:
                print combination
                self._words.append(combination)
