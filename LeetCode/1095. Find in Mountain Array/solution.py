# class Solution:
#     def findInMountainArray(self, secret: List[int], target: int) -> int:
#         def findPeak():
#             n = len(secret)
#             left, right = 0, n-2
#             while left+1 < right:
#                 mid = (left+right)//2
#                 if secret[mid] < secret[mid+1]:
#                     left = mid
#                 else:
#                     right = mid
#             return right
        
#         peak = findPeak()
        
#         # print(peak)
        
#         left, right = 0, peak+1
#         # if secret[right] == target:
#         #     return right
#         while left < right:
#             mid = (left+right)//2
#             if secret[mid] == target:
#                 return mid
#             elif secret[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid
        
#         left, right = peak, len(secret)
#         # if secret[right] == target:
#         #     return right
#         while left < right:
#             mid = (left+right)//2
#             if secret[mid] == target:
#                 return mid
#             elif secret[mid] > target:
#                 left = mid+1
#             else:
#                 right = mid
                
#         return -1
            
#         

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        lo, hi = 0, n-1
        while hi - lo > 2:
            mid = (lo+hi)//2
            if mountain_arr.get(mid+1) > mountain_arr.get(mid):
                lo = mid
            else:
                hi = mid
        peak = lo + 1
        # print(lo,peak,hi)
        def search(left, right, dsc):
            while left <= right:
                mid = (left+right)//2
                if mountain_arr.get(mid) == target:
                    return mid
                elif (mountain_arr.get(mid) > target)^dsc:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        idx = search(0,peak,False)
        if idx > -1:
            return idx
        return search(peak,n-1,True)