class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        res, idx1, idx2 = float('inf'), -float('inf'), -float('inf')
        for i, word in enumerate(words):
            if word == word1:
                res = min(res, i-idx2)
                idx1 = i 
            elif word == word2:
                res = min(res, i-idx1)
                idx2 = i 
        return res 