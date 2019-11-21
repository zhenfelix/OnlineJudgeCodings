# class WordDistance:

#     def __init__(self, words: List[str]):
#         self.dis = collections.defaultdict(int)
#         self.wordset = collections.defaultdict(int)
#         for i, word in enumerate(words):
#             for k, j in self.wordset.items():
#                 self.dis[word,k] = min(self.dis.get((word,k),float('inf')), i-j)
#                 self.dis[k,word] = min(self.dis.get((k,word),float('inf')), i-j)
#             self.wordset[word] = i 


#     def shortest(self, word1: str, word2: str) -> int:
#         return self.dis[word1,word2]
        

# class WordDistance:

#     def __init__(self, words: List[str]):
#         self.dis = collections.defaultdict(int)
#         self.wordset = collections.defaultdict(list)
#         for i, word in enumerate(words):
#             self.wordset[word].append(i) 


#     def shortest(self, word1: str, word2: str) -> int:
#         if (word1,word2) not in self.dis:
#             res = float('inf')
#             for i in self.wordset[word1]:
#                 for j in self.wordset[word2]:
#                     res = min(res, abs(i-j))
#             self.dis[word1,word2] = res
#             self.dis[word2,word1] = res
#         return self.dis[word1,word2]

# class WordDistance:

#     def __init__(self, words: List[str]):
#         self.dis = collections.defaultdict(int)
#         self.wordset = collections.defaultdict(list)
#         for i, word in enumerate(words):
#             self.wordset[word].append(i) 


#     def shortest(self, word1: str, word2: str) -> int:
#         if (word1,word2) not in self.dis:
#             res = float('inf')
#             i, j = 0, 0
#             pre, flag = -float('inf'), True
#             while i < len(self.wordset[word1]) and j < len(self.wordset[word2]):
#                 if self.wordset[word1][i] < self.wordset[word2][j]:
#                     if not flag:
#                         res = min(res, self.wordset[word1][i]-pre)
#                     pre, flag = self.wordset[word1][i], True
#                     i += 1
#                 else:
#                     if flag:
#                         res = min(res, self.wordset[word2][j]-pre)
#                     pre, flag = self.wordset[word2][j], False
#                     j += 1
#             if i < len(self.wordset[word1]):
#                 res = min(res, self.wordset[word1][i]-pre)
#             else:
#                 res = min(res, self.wordset[word2][j]-pre)

#             self.dis[word1,word2] = res
#             self.dis[word2,word1] = res
#         return self.dis[word1,word2]

class WordDistance:

    def __init__(self, words: List[str]):
        self.dis = collections.defaultdict(int)
        self.wordset = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.wordset[word].append(i) 


    def shortest(self, word1: str, word2: str) -> int:
        if (word1,word2) not in self.dis:
            res = float('inf')
            i, j = 0, 0
            while i < len(self.wordset[word1]) and j < len(self.wordset[word2]):
                res = min(res, abs(self.wordset[word1][i]-self.wordset[word2][j]))
                if self.wordset[word1][i] < self.wordset[word2][j]:
                    i += 1
                else:
                    j += 1
            
            self.dis[word1,word2] = res
            self.dis[word2,word1] = res
        return self.dis[word1,word2]