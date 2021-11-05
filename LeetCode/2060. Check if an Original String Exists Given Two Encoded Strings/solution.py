class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        dp = [[set() for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0].add(0)
        for i in range(n+1):
            for j in range(m+1):
                for delta in dp[i][j]:
                    num = 0
                    for k in range(i,min(i+3,n)):
                        if s1[k].isdigit():
                            num = num*10 + ord(s1[k]) - ord('0')
                            dp[k+1][j].add(delta+num)
                        else:
                            break
                    num = 0 
                    for k in range(j,min(j+3,m)):
                        if s2[k].isdigit():
                            num = num*10 + ord(s2[k]) - ord('0')
                            dp[i][k+1].add(delta-num)
                        else:
                            break
                    if i < n and not s1[i].isdigit() and delta < 0:
                        dp[i+1][j].add(delta+1)
                    if j < m and not s2[j].isdigit() and delta > 0:
                        dp[i][j+1].add(delta-1)
                    if i < n and j < m and delta == 0 and s1[i] == s2[j]:
                        dp[i+1][j+1].add(0)
        return 0 in dp[-1][-1]



class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        
        def gg(s): 
            """Return possible length."""
            ans = {int(s)}
            for i in range(1, len(s)): 
                ans |= {x+y for x in gg(s[:i]) for y in gg(s[i:])}
            return ans
        
        @cache
        def fn(i, j, diff): 
            """Return True if s1[i:] matches s2[j:] with given differences."""
            if i == len(s1) and j == len(s2): return diff == 0
            if i < len(s1) and s1[i].isdigit(): 
                ii = i
                while ii < len(s1) and s1[ii].isdigit(): ii += 1
                for x in gg(s1[i:ii]): 
                    if fn(ii, j, diff-x): return True 
            elif j < len(s2) and s2[j].isdigit(): 
                jj = j 
                while jj < len(s2) and s2[jj].isdigit(): jj += 1
                for x in gg(s2[j:jj]): 
                    if fn(i, jj, diff+x): return True 
            elif diff == 0: 
                if i < len(s1) and j < len(s2) and s1[i] == s2[j]: return fn(i+1, j+1, 0)
            elif diff > 0: 
                if i < len(s1): return fn(i+1, j, diff-1)
            else: 
                if j < len(s2): return fn(i, j+1, diff+1)
            return False 
            
        return fn(0, 0, 0)







# class Solution:
#     def possiblyEquals(self, s1: str, s2: str) -> bool:
#         def dfs(i, s, path, res):
#             if i == len(s):
#                 sz = 0
#                 for a in path:
#                     if a.isdigit():
#                         sz += int(a)
#                     else:
#                         sz += len(a)
#                 res[sz].append(path)
#                 return
#             if s[i].isdigit():
#                 dfs(i+1, s, path+[s[i]], res)
#                 if path and path[-1].isdigit():
#                     dfs(i+1, s, path[:-1]+[path[-1]+s[i]], res)
#             else:
#                 if path and not path[-1].isdigit():
#                     dfs(i+1, s, path[:-1]+[path[-1]+s[i]], res)
#                 else:
#                     dfs(i+1, s, path+[s[i]], res)
#             return
#         left = defaultdict(list)
#         right = defaultdict(list)
#         dfs(0,s1,[],left)
#         dfs(0,s2,[],right)
#         # print(left)
#         # print(right)
#         def check(p1,p2):
#             def generate(p, mp):
#                 sz = 0
#                 for a in p:
#                     if a.isdigit():
#                         sz += int(a)
#                     else:
#                         for i, ch in enumerate(a):
#                             mp[sz+i] = ch 
#                         sz += len(a)
#                 return
#             mp1 = dict()
#             mp2 = dict()
#             generate(p1, mp1)
#             generate(p2, mp2)
#             # print(mp1,mp2)
#             for k, v in mp1.items():
#                 if k in mp2 and v != mp2[k]:
#                     return False
#             for k, v in mp2.items():
#                 if k in mp1 and v != mp1[k]:
#                     return False
#             return True

#         for k, v1 in left.items():
#             v2 = right[k]
#             if any(check(p1,p2) for p1 in v1 for p2 in v2):
#                 # print(v1, v2)
#                 return True

#         return False

