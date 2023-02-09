
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cc = Counter([a%k for a in arr])
        if cc[0]%2:
            return False
        l, r = 1, k-1
        while l < r:
            if cc[l] != cc[r]:
                return False
            l += 1
            r -= 1
        return True
        
# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         cc = Counter([a%k for a in arr])
#         if cc[0]%2:
#             return False
#         l, r = 1, k-1
#         while l <= r:
#             if l == r:
#                 if cc[l]%2:
#                     return False
#             else:
#                 if cc[l] != cc[r]:
#                     return False
#             l += 1
#             r -= 1
#         return True