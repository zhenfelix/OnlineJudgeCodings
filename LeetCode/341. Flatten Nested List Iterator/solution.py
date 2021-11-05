# # """
# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
# # """
# #class NestedInteger(object):
# #    def isInteger(self):
# #        """
# #        @return True if this NestedInteger holds a single integer, rather than a nested list.
# #        :rtype bool
# #        """
# #
# #    def getInteger(self):
# #        """
# #        @return the single integer that this NestedInteger holds, if it holds a single integer
# #        Return None if this NestedInteger holds a nested list
# #        :rtype int
# #        """
# #
# #    def getList(self):
# #        """
# #        @return the nested list that this NestedInteger holds, if it holds a nested list
# #        Return None if this NestedInteger holds a single integer
# #        :rtype List[NestedInteger]
# #        """

# class NestedIterator(object):

#     def __init__(self, nestedList):
#         """
#         Initialize your data structure here.
#         :type nestedList: List[NestedInteger]
#         """
#         self.st = nestedList[::-1]

#     def next(self):
#         """
#         :rtype: int
#         """
#         return self.st.pop().getInteger()
        

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         while self.st:
#             if self.st[-1].isInteger():
#                 return True
#             self.st.extend(self.st.pop().getList()[::-1])
#         return False   

# # Your NestedIterator object will be instantiated and called as such:
# # i, v = NestedIterator(nestedList), []
# # while i.hasNext(): v.append(i.next())

# class NestedIterator(object):

#     def __init__(self, nestedList):
#         def gen(nestedList):
#             for x in nestedList:
#                 if x.isInteger():
#                     yield x.getInteger()
#                 else:
#                     for y in gen(x.getList()):
#                         yield y
#         self.gen = gen(nestedList)

#     def next(self):
#         return self.value

#     def hasNext(self):
#         try:
#             self.value = next(self.gen)
#             return True
#         except StopIteration:
#             return False

class NestedIterator(object):

    def __init__(self, nestedList):
        self.peek = None
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y
        self.gen = gen(nestedList)

    def next(self):
        if self.peek is None:
            return next(self.gen)
        else:
            tmp = self.peek
            self.peek = None
            return tmp
                

    def hasNext(self):
        if self.peek is None:
            try:
                self.peek = next(self.gen)
                return True
            except StopIteration:
                return False
        else:
            return True



class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st = nestedList[::-1]
    
    def next(self) -> int:
        return self.st.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.st:
            cur = self.st[-1]
            if cur.isInteger():
                return True
            self.st.pop()
            q = cur.getList()
            for nxt in q[::-1]:
                self.st.append(nxt)
        return False
         