class Solution:
    def findMinStep(self, board, hand):   
        def dfs(s, c):
            if not s: return 0
            res, i = float("inf"), 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[i] == s[j]: j += 1
                incr = 3 - (j - i)
                if c[s[i]] >= incr:
                    incr = 0 if incr < 0 else incr
                    c[s[i]] -= incr
                    tep = dfs(s[:i] + s[j:], c)
                    res = min(res, tep + incr)
                    c[s[i]] += incr
                i = j
            return res 
        ans = dfs(board, collections.Counter(hand))
        return ans if ans != float("inf") else -1