class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(s):
            cur = 0
            for ch in s:
                cur = cur*10 + ord(ch)-ord('a')
            return cur
        return convert(firstWord)+convert(secondWord) == convert(targetWord)