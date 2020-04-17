class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        state = [float('inf')]*(2**5)
        state[0] = -1
        mp = {'a':0,'e':1,'i':2,'o':3,'u':4}
        res, cur = 0, 0
        for i,ch in enumerate(s):
            if ch in "aeiou":
                cur ^= (1<<mp[ch])
                state[cur] = min(state[cur],i)
            res = max(res,i-state[cur])
        return res
        