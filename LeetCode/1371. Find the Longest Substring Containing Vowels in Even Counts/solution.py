class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        t = "aeiou"
        mp = {ch: i for i, ch in enumerate(t)}
        pos = {0: -1}
        ans, cur = 0, 0
        for i, ch in enumerate(s):
            if ch in t:
                cur ^= (1<<mp[ch])
            if cur in pos:
                ans = max(ans, i-pos[cur])
            else:
                pos[cur] = i 
        return ans

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
        