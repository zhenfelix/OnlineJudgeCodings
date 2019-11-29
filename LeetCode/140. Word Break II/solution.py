# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         n = len(s)
#         dp = [[] for _ in range(n+1)]
#         dp[0] = ['']
#         for i in range(n):
#             for j in range(i+1,n+1):
#                 if s[i:j] in wordDict:
#                     for sentence in dp[i]:
#                         dp[j].append(sentence+" "+s[i:j])
#             # for word in wordDict:
#             #     if s[i:].startswith(word):
#             #         for sentence in dp[i]:
#             #             dp[i+len(word)].append(sentence+" "+word)
#         return [sentence[1:] for sentence in dp[-1]]

# class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    #     n = len(s)
    #     dp = [[] for _ in range(n+1)]
    #     dp[0] = [[]]
    #     for i in range(n):
    #         for idx, word in enumerate(wordDict):
    #             if len(dp[i]) > 0 and s[i:].startswith(word):
    #                 dp[i+len(word)].append(idx)
    #     def dfs(idx, path):
    #         if idx == 0:
    #             res.append(' '.join(map(lambda x:wordDict[x], path[::-1])))
    #             return
    #         for item in dp[idx]:
    #             dfs(idx-len(wordDict[item]),path+[item])
    #         return
    #     # print(dp)
    #     res = []
    #     dfs(n,[])
    #     return res
    
    

# class Solution:
#     def wordBreak(self, s, wordDict):
#         memo = {len(s): ['']}
#         def sentences(i):
#             if i not in memo:
#                 memo[i] = [s[i:j] + (tail and ' ' + tail)
#                            for j in range(i+1, len(s)+1)
#                            if s[i:j] in wordDict
#                            for tail in sentences(j)]
#             return memo[i]
#         return sentences(0)


from functools import lru_cache
class Solution:
    def wordBreak(self, s, wordDict):
        @lru_cache(None)
        def sentences(i):
            if i == len(s):
                return ['']
            res = [s[i:j] + (tail and ' ' + tail)
                       for j in range(i+1, len(s)+1)
                       if s[i:j] in wordDict
                       for tail in sentences(j)]
            return res
        wordDict = set(wordDict)
        return sentences(0)