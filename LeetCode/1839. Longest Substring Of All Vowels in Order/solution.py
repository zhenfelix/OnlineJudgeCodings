class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        mp = {ch: i+1 for i, ch in enumerate("aeiou")}
        s, cnt, res = 0, 0, 0
        for ch in word:
            ch = mp[ch]
            if s <= ch <= s+1:
                cnt += 1
                s = ch 
            elif ch == 1:
                cnt = 1
                s = ch
            else:
                cnt = 0
                s = 0
            if s == 5:
                res = max(res, cnt)
        return res

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