# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def dfs(pos, cur):
#             if pos == n:
#                 return cur.ending >= 0
#             if cur.ending >= 0:
#                 if dfs(pos+1, tree.root):
#                     return True
#             ch = s[pos]
#             if ch in cur.children:
#                 return dfs(pos+1, cur.children[ch])
#             return False

#         tree = Trie()
#         n = len(s)
#         for i in range(len(wordDict)):
#             tree.insert(i,wordDict)
#         return dfs(0,tree.root)


# class Trie:
#     def __init__(self):
#         self.root = Node()

#     def insert(self, idx, wordDict):
#         word = wordDict[idx]
#         cur = self.root
#         for w in word:
#             if w not in cur.children:
#                 cur.children[w] = Node()
#             cur = cur.children[w]
#         cur.ending = idx

# class Node:
#     def __init__(self):
#         self.children = {}
#         self.ending = -1


# from functools import lru_cache
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         @lru_cache(None)
#         def dfs(idx):
#             if idx == n:
#                 return True
#             for word in wordDict:
#                 if s[idx:].startswith(word) and dfs(idx+len(word)):
#                     return True
#             return False

#         n = len(s)
#         return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            for word in wordDict:
                if s[i:].startswith(word):
                    dp[i+len(word)] = True
        return dp[-1]

        
        
        
        
        
