# -*- coding: utf-8 -*-
#
# Dict Cleaner
#
# Cleans dictionary - removes words other than nouns
#
#


if __name__ == '__main__':
    dictionary = ''
    with open('nouns.txt') as f:
        for word in f.readlines():
            w = word[:-2]
            if (
                not w.endswith('suffix to remove')
            ):
                dictionary += word
            else:
                print w

    with open('nouns.txt', 'w') as f:
        f.write(dictionary)
