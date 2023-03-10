class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        mp = dict()
        for i in range(n)[::-1]:
            if s[i] == '0': 
                mp[0] = (i,i)
                continue
            v = 0
            for j in range(i,min(n,i+40)):
                v = (v<<1)|int(s[j])
                mp[v] = (i,j)
        ans = []
        for a, b in queries:
            x = a^b 
            if x not in mp:
                ans.append([-1,-1])
            else:
                l, r = mp[x]
                ans.append([l,r])
        return ans 