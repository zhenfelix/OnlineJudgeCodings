class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        cnt = 0
        for word in words:
            if all(ch not in brokenLetters for ch in word):
                cnt += 1
        return cnt 