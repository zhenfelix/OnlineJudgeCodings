# class CombinationIterator:

#     def __init__(self, characters: str, combinationLength: int):
#         self.state = [i for i in range(combinationLength)]
#         self.characters = characters
        

#     def next(self) -> str:
#         res = ""
#         for s in self.state:
#             res += self.characters[s]
#         n, m = len(self.characters), len(self.state)
#         idx = m-1
#         while idx >= 0 and self.state[idx]+1==n-(m-1-idx):
#             self.state[idx] = -1
#             idx -= 1
#         if idx == -1:
#             return res
#         self.state[idx] += 1
#         idx += 1
#         while idx <= m-1:
#             self.state[idx] = self.state[idx-1]+1
#             idx += 1
#         return res
        

#     def hasNext(self) -> bool:
#         return self.state[0] != -1
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class CombinationIterator(object):

    def __init__(self, A, k):
        self.it = itertools.combinations(A, k)
        self.last = A[-k:]
        self.hasNext = lambda: True

    def next(self):
        res = ''.join(next(self.it))
        self.hasNext = lambda: res != self.last
        return res
        

    def hasNext(self) -> bool:
        return self.hasNext


# class CombinationIterator(object):

#     def __init__(self, characters, combinationLength):
#         """
#         :type characters: str
#         :type combinationLength: int
#         """
#         self.char = characters
#         self.comb = combinationLength
#         self.cur = 0
        
#         self.comblist = [] # ['ab','ac','bc'] # populate the list with combinationLength
#         self.helper('', 0, self.comb, self.comblist,0)
 
        
#     def helper(self, strin , ind, cap, res, cumu):
#         if cumu == cap:
#             res.append(strin)
#             return 
#         for i in range(ind, len(self.char)):
#             self.helper( strin + self.char[i] , i+1, cap,res, cumu+1 )
  
 
        
#     def next(self):
#         """
#         :rtype: str
#         """
#         self.cur += 1
#         return self.comblist[self.cur - 1]
        
        

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.cur < len(self.comblist) 