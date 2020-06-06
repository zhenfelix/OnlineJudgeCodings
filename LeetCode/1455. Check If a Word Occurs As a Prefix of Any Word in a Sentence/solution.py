class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        n = len(searchWord)
        res = -1
        for i, word in enumerate(sentence,1):
            if word[:n] == searchWord:
                res = i
                break
        return res
