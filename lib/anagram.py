# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
    def match(self, possible_anagrams):
        matches = []
        for possible_anagram in possible_anagrams:
            if possible_anagram.lower() != self.word and sorted(possible_anagram.lower()) == self.sorted_word:
                matches.append(possible_anagram)
        return matches