class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []

        for w in words:
            if sorted(w) == sorted(self.word) and w != self.word:
                anagrams.append(w)

        return anagrams


