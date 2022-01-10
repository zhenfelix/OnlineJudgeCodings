class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        for word in startWords:
            cur = 0
            for ch in word:
                j = ord(ch)-ord('a')
                cur |= (1<<j)
            for i in range(26):
                if (cur>>i)&1 == 0:
                    seen.add(cur|(1<<i))
        res = 0
        for word in targetWords:
            cur = 0
            for ch in word:
                j = ord(ch)-ord('a')
                cur |= (1<<j)
            if cur in seen:
                res += 1
        return res


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        for word in startWords:
            cc = Counter(word)
            for i in range(26):
                ch = chr(ord('a')+i)
                if cc[ch] == 0:
                    seen.add(''.join(sorted(word+ch)))
        res = 0
        for word in targetWords:
            if ''.join(sorted(word)) in seen:
                res += 1
        return res
