class Solution:
#     def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
#         m, n =len(req_skills), len(people)
#         rqsk = 0
#         mp = {}
#         for i in range(m):
#             rqsk |= (1<<i)
#             mp[req_skills[i]] = (1<<i)
#         dp = {}
#         def dfs(idx, remains):
#             if (idx, remains) in dp:
#                 return dp[idx,remains]
#             old_remains = remains
#             if idx >= 0:
#                 for s in people[idx]:
#                     if mp[s] & remains > 0:
#                         remains -= mp[s]
                        
#                 if remains == 0:
#                     dp[idx,remains] = [idx]
#                     return dp[idx,remains]
    
#             candidates = [-1]*(n+1)
#             for i in range(idx+1, n):
#                 tmp = dfs(i,remains)
#                 if len(tmp) < len(candidates):
#                     candidates = tmp.copy()
#             dp[idx,old_remains] = [idx]+candidates
#             return dp[idx,old_remains]
            
            
#         ans = dfs(-1,rqsk)
#         return ans[1:]
            

    def smallestSufficientTeam(self, req_skills, people):
        n, m = len(req_skills), len(people)
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            for skill_set, need in dp.copy().items():
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]