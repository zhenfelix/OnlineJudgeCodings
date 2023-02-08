class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = list(map(lambda x: ''.join(sorted(set(list(x)))), words))
        cc = Counter()
        ans = 0
        for w in words:
            ans += cc[w]
            cc[w] += 1 
        return ans 