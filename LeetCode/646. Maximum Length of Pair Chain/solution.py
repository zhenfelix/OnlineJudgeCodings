class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # pairs.sort(key = lambda x: (x[1], x[0]))
        pairs.sort(key = lambda x: (x[1],-x[0]))
        # print(pairs)
        cnt, cur = 0, -float("inf")
        for s, e in pairs:
            if s > cur:
                cnt += 1
                cur = e 
        return cnt