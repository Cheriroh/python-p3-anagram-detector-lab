# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store word in lowercase for consistency

    def match(self, word_list):
        # Sort the letters of the original word
        sorted_word = sorted(self.word)

        # Find words that match the sorted version
        anagrams = [word for word in word_list if sorted(word.lower()) == sorted_word]

        return anagrams
