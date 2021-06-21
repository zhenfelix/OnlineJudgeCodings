class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp = defaultdict(int)
        n = len(words)
        for word in words:
            for ch in word:
                mp[ch] += 1
        for ch in range(26):
            ch = chr(ch+ord('a'))
            if mp[ch]%n != 0:
                return False
        return True
