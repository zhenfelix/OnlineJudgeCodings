# from collections import deque

# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         if endWord not in wordList:
#             return []
#         paths = {}
#         mp = {}
#         for word in wordList+[beginWord]:
#             paths[word] = []
#             for i,ch in enumerate(word):
#                 tmp = word[:i]+'*'+word[i+1:]
#                 if tmp not in mp:
#                     mp[tmp] = [word]
#                 else:
#                     mp[tmp] += [word]
                
        
#         # print('mp: ', mp)
#         visited = set()
#         q = deque()
#         q.append(beginWord)
#         paths[beginWord] += [[beginWord]]
#         visited.add(beginWord)
        
#         while(len(q) > 0):
#             # print(q)
#             n = len(q)
#             visited_tmp = visited.copy()
#             for _ in range(n):
#                 word = q.popleft()
#                 # print(word)
#                 for i,ch in enumerate(word):
#                     for tmp in mp[word[:i]+'*'+word[i+1:]]:
#                         if tmp not in visited:
#                             paths[tmp] += [path+[tmp] for path in paths[word]]
#                             if tmp not in visited_tmp:
#                                 q.append(tmp)
#                                 visited_tmp.add(tmp)
          
#             visited = visited_tmp
        
#         # print(paths)
#         return paths[endWord]
                        
                        

        
# The only tricky thing you need to remember is this is a BFS of paths not words!

        
from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        mp = {}
        for word in wordList+[beginWord]:
            for i,ch in enumerate(word):
                tmp = word[:i]+'*'+word[i+1:]
                if tmp not in mp:
                    mp[tmp] = [word]
                else:
                    mp[tmp] += [word]
                
        
        # print('mp: ', mp)
        paths = deque()
        visited = set()
        paths.append([beginWord])
        visited.add(beginWord)
        ans = []
        
        while(len(paths) > 0):
            # print(q)
            n = len(paths)
            if len(ans) > 0:
                break
            visited_cp = visited.copy()
            for _ in range(n):
                path = paths.popleft()
                word = path[-1]
                for i,ch in enumerate(word):
                    for tmp in mp[word[:i]+'*'+word[i+1:]]:
                        if tmp == endWord:
                            ans += [path+[tmp]]
                        elif tmp not in visited:
                            paths.append(path+[tmp])
                            visited_cp.add(tmp)
            visited = visited_cp
        
        return ans
                        