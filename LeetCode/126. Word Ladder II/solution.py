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



# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         mp = collections.defaultdict(list)
#         for word in wordList:
#             for i in range(len(word)):
#                 mp[word[:i]+"*"+word[i+1:]].append(word)
#         res = []
#         pre = collections.defaultdict(list)
#         visited = collections.defaultdict(int)
#         visited[beginWord] = -1
#         q = collections.deque([beginWord])
#         level = 0
#         print(mp)
#         while q:
#             n = len(q)
#             print(q)
#             for _ in range(n):
#                 word = q.popleft()
#                 if word == endWord:
#                     break
#                 for i in range(len(word)):
#                     key = word[:i]+"*"+word[i+1:]
#                     for nxt in mp[key]:
#                         if level <= visited.get(nxt,float("inf")):
#                             pre[nxt].append(word)
#                             if level < visited.get(nxt,float("inf")):
#                                 visited[nxt] = level
#                                 q.append(nxt)
#             level += 1
            
#         # print(pre)
#         # print(mp)
#         if not pre[endWord]:
#             # print("ok")
#             return []
#         def dfs(path):
#             # print(path)
#             cur = path[-1]
#             if not pre[cur]:
#                 res.append(path[::-1].copy())
#             for nxt in pre[cur]:
#                 dfs(path+[nxt])
#             return
#         # dfs([endWord])
#         return res
                       

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        wordList = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                mp[word[:i]+"*"+word[i+1:]].append(word)
        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]
        while layer:
            layer_new = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[endWord]
                for i in range(len(word)):
                    key = word[:i]+"*"+word[i+1:]
                    for nxt in mp[key]:
                        if nxt in wordList:
                            layer_new[nxt].extend(path+[nxt] for path in layer[word])
                            
            wordList -= set(layer_new.keys())
            layer = layer_new
            
        return []

    
# class Solution(object):
#     def findLadders(self, beginWord, endWord, wordList):

#         wordList = set(wordList)
#         res = []
#         layer = {}
#         layer[beginWord] = [[beginWord]]

#         while layer:
#             newlayer = collections.defaultdict(list)
#             for w in layer:
#                 if w == endWord: 
#                     # res.extend(k for k in layer[w])
#                     return layer[w]
#                 else:
#                     for i in range(len(w)):
#                         for c in 'abcdefghijklmnopqrstuvwxyz':
#                             neww = w[:i]+c+w[i+1:]
#                             if neww in wordList:
#                                 newlayer[neww]+=[j+[neww] for j in layer[w]]

#             wordList -= set(newlayer.keys())
#             layer = newlayer

#         return res