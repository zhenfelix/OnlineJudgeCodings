from collections import deque

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        
#         q = deque()
#         q.append(beginWord)
#         toVisit = set(wordList)
#         # toVisit.remove(beginWord)
#         dist = 1
#         while len(q) > 0:
#             n = len(q)
#             # print(q)
#             for _ in range(n):
#                 cur = q.popleft()
#                 if cur == endWord:
#                     return dist
#                 for i, _ in enumerate(cur):
#                     for j in range(26):
#                         ch = chr(ord('a')+j)
#                         candidate = cur[:i]+ch+cur[i+1:]
#                         if candidate in toVisit:
#                             q.append(candidate)
#                             toVisit.remove(candidate)
#                 # for candidate in toVisit.copy():
#                 #     if isLinked(cur, candidate):
#                 #         q.append(candidate)
#                 #         toVisit.remove(candidate)
#             dist += 1
#         return 0

## bidirectional bfs
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:        
#         head, tail = set(), set()
#         head.add(beginWord)
#         tail.add(endWord)
#         toVisit = set(wordList)
#         if endWord not in toVisit:
#             return 0
#         toVisit.remove(endWord)
#         ladder = 2
#         while len(head) > 0 and len(tail) > 0:
#             if len(head) > len(tail):
#                 head, tail = tail, head
#             n = len(head)
#             # print('head', head)
#             # print('tail', tail)
#             tmp = set()
#             for cur in head:
#                 # if cur in tail:
#                 #     return ladder
#                 for i, _ in enumerate(cur):
#                     for j in range(26):
#                         ch = chr(ord('a')+j)
#                         candidate = cur[:i]+ch+cur[i+1:]
#                         if candidate in tail:
#                             return ladder
#                         if candidate in toVisit:
#                             tmp.add(candidate)
#                             toVisit.remove(candidate)
#             head = tmp
#             ladder += 1
#         # print('oops')
#         return 0


##list preprocessing and BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(wordList + [beginWord])
        return bfs_words(beginWord, endWord, d)