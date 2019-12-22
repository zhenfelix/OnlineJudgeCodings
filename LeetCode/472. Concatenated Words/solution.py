# class Node:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False

# class Trie:
#     def __init__(self):
#         self.root = Node()

#     def insert(self, word):
#         cur = self.root
#         for w in word:
#             if w not in cur.children:
#                 cur.children[w] = Node()
#             cur = cur.children[w]
#         cur.isWord = True
#         return

# from functools import lru_cache
# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         tree = Trie()
#         for word in words:
#             tree.insert(word)

#         @lru_cache(None)
#         def dfs(i, cur):
#             # print(i,cur.children)
#             if i == len(word):
#                 return 1 if cur.isWord else 0

#             if cur.isWord and dfs(i,tree.root) > 0:
#                 return 1+dfs(i,tree.root)
#             if word[i] not in cur.children:
#                 return 0
#             return dfs(i+1, cur.children[word[i]])

#         res = []
#         for word in words:
#             # print(word)
#             # print(dfs(0,tree.root))
#             if dfs(0,tree.root) > 1:
#                 res.append(word)
#             dfs.cache_clear()
#         return res
        
from functools import lru_cache
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)
        @lru_cache(None)
        def dfs(start):
            for i in range(start+1, len(word)):
                prefix = word[start:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(i):
                    return True
             
            
            return False
        
        res = []
        for word in words:
            if dfs(0):
                res.append(word)
            dfs.cache_clear()
        
        return res