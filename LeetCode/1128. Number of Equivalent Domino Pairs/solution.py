class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mp = {}
        ans = 0
        for a in dominoes:
            tmp = (1<<a[0]) | (1<<a[1])
            if tmp not in mp:
                mp[tmp] = 1
            else:
                mp[tmp] += 1
            ans += (mp[tmp]-1)
        return ans