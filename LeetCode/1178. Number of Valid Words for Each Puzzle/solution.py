# import collections

# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         def dfs(idx, cur):
#             if idx == len(t):
#                 return word_set[cur]

#             cc = 0
#             cc += dfs(idx+1, cur)
#             cc += dfs(idx+1, cur|t[idx])
#             return cc        

#         word_set = collections.Counter()
#         for word in words:
#             t = 0
#             for w in word:
#                 t |= (1<<(ord(w)-ord('a')))
#             word_set[t] += 1
            
#         ans = []
#         for puzzle in puzzles:
#             t = [1<<(ord(x)-ord('a')) for x in list(puzzle)]
#             ans.append(dfs(1,t[0]))
#         return ans

    
import collections

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:   
        count = collections.Counter()
        for w in words:
            m = 0
            for c in w:
                m |= 1 << (ord(c) - 97)
            count[m] += 1
        res = []
        for p in puzzles:
            bfs = [1 << (ord(p[0]) - 97)]
            for c in set(p[1:]):
                bfs += [m | 1 << (ord(c) - 97) for m in bfs]
            res.append(sum(count[m] for m in bfs))
        return res
    
    
# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         word_set = []
#         for word in words:
#             t = 0
#             for w in word:
#                 t |= (1<<(ord(w)-ord('a')))
#             word_set.append(t)
        
#         n = len(words)
#         ans = []
#         for puzzle in puzzles:
#             t = 0
#             for p in puzzle:
#                 t |= (1<<(ord(p)-ord('a')))
            
#             cc = 0
#             for i in range(n):
#                 if (word_set[i] | t) == t and (word_set[i] & (1<<(ord(puzzle[0])-ord('a')))):
#                     cc += 1
#             ans.append(cc)
        
#         return ans

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.count = 0


# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         # def dfs(node, idx, firstSeen, path):
#         #     # print(node, idx, firstSeen)
#         #     if idx >= len(puzzle):
#         #         return 0
#         #     cc = 0
#         #     if firstSeen:
#         #         cc = node.count
#         #         print(path, cc)
#         #     if puzzle[idx] == first:
#         #         firstSeen = True
#         #     else:
#         #         cc += dfs(node, idx+1, firstSeen, path)
#         #     if puzzle[idx] in node.children:
#         #         cc += dfs(node.children[puzzle[idx]], idx+1, firstSeen, path+puzzle[idx])
#         #     # cc += dfs(node, idx+1, firstSeen)
#         #     return cc
        
#         def dfs(node, idx, firstSeen):
#             cc = 0
#             if firstSeen:
#                 cc = node.count
#                 # print(path, cc)
#             for i in range(idx,len(puzzle)):
#                 if puzzle[i] not in node.children:
#                     continue
#                 if puzzle[i] == first:
#                     cc += dfs(node.children[puzzle[i]], i+1, True)
#                     break
#                 else:
#                     cc += dfs(node.children[puzzle[i]], i+1, firstSeen)
#             return cc
        
        
#         root = TrieNode()
        
#         for word in words:
#             tmp = set()
#             for w in word:
#                 tmp.add(w)
#             cur = root
#             for ch in sorted(tmp):
#                 if ch not in cur.children:
#                     cur.children[ch] = TrieNode()
#                 cur = cur.children[ch]
#             cur.count += 1
        
        
#         ans = []
#         for puzzle in puzzles:
#             tmp = set()
#             for p in puzzle:
#                 tmp.add(p)
#             first = puzzle[0]
#             puzzle = sorted(tmp)
#             # print(puzzle, first)
#             ans.append(dfs(root,0,False))
            
#         return ans
            