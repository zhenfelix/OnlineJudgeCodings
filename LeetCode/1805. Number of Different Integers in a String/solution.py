class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = [ch if "0" <= ch <= "9" else " " for ch in word]
        # print(set(map(int,filter(None,"".join(word).split(" ")))))
        return len(set(map(int,"".join(word).split())))