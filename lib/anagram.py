class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        #start with sorting the letters of the initial word
        sorted_word = sorted(self.word)
        matches = []

        #iterate through the list of words
        
        for word in word_list:
            #if the sorted words are the same, add to matches
            if sorted(word) == sorted_word:
                matches.append(word)
                
        return matches