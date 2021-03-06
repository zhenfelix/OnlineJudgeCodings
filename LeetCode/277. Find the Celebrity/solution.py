# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# class Solution(object):
#     def findCelebrity(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         a, b = 0, 1
#         while b < n:
#             ab, ba = knows(a,b), knows(b,a)
#             if not ab ^ ba:
#                 a, b = b+1, b+2
#             elif ab:
#                 a, b = b, b+1
#             else:
#                 b = b+1
#         if a < n:
#             for i in range(n):
#                 if i == a:
#                     continue
#                 if not knows(i,a) or knows(a,i):
#                     return -1
#             return a
#         return -1

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1,n):
            if knows(candidate,i):
                candidate = i 
        for i in range(n):
            if i == candidate:
                continue
            if not knows(i,candidate) or knows(candidate,i):
                return -1
        return candidate

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidates = set([i for i in range(n)])
        while len(candidates) > 1:
            a, b = candidates.pop(), candidates.pop()
            ab, ba = knows(a,b), knows(b,a)
            if ab ^ ba:
                if ab:
                    candidates.add(b)
                else:
                    candidates.add(a)
        if not candidates:
            return -1
        cur = candidates.pop()
        for i in range(n):
            if i == cur:
                continue
            if knows(cur,i) or not knows(i,cur):
                return -1
        return cur