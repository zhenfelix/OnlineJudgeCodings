# class MagicDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.mp = defaultdict(set)

#     def generate(self, s):
#         n = len(s)
#         for i in range(n):
#             yield s[:i]+'*'+s[i+1:]

#     def buildDict(self, dictionary: List[str]) -> None:
#         for word in dictionary:
#             for w_ in self.generate(word):
#                 self.mp[w_].add(word)

#     def search(self, searchWord: str) -> bool:
#         return any(len(self.mp[w_]) > 1 or (self.mp[w_] and searchWord not in self.mp[w_]) for w_ in self.generate(searchWord))
        


# # Your MagicDictionary object will be instantiated and called as such:
# # obj = MagicDictionary()
# # obj.buildDict(dictionary)
# # param_2 = obj.search(searchWord)


class MagicDictionary(object):
    def _candidates(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]
            
    def buildDict(self, words):
        self.words = set(words)
        self.near = collections.Counter(cand for word in words
                                        for cand in self._candidates(word))

    def search(self, word):
        return any(self.near[cand] > 1 or 
                   self.near[cand] == 1 and word not in self.words
                   for cand in self._candidates(word))