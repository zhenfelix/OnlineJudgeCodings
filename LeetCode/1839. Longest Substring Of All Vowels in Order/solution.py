class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res, cur = 0, 0
        pre = {'e':'a', 'i':'e', 'o':'i', 'u':'o'}
        for i, ch in enumerate(word):
            if ch == 'a':
                if i and word[i-1] != ch:
                    cur = 1
                else:
                    cur += 1
            else:
                if i and (word[i-1] == ch or word[i-1] == pre[ch]) and cur:
                    cur += 1
                else:
                    cur = 0
                if ch == 'u':
                    res = max(res, cur)
        return res