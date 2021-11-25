"""Word Finder: finds random words from a dictionary."""

import random
    #we pull in the library itself

class WordFinder:
    ...
    #first we need to read from the dictionary
    def __init__(self, path):
        dict_file = open(path)

        self.words = self.parse(dict_file)
        #need to parse the dictionary first

    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random (self):
        return random.choice(self.words)
        #from random, pull in 'choice' function as choice
        #we now are able to pull from the parsed dictionary and then randomly choose a word


