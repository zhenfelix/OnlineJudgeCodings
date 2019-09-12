class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        n = len(bulbs)
        if n < 3 or K > n-2:
            return -1
        K += 1
        minBucket = [float('inf')]*(n//K+1)
        maxBucket = [-float('inf')]*(n//K+1)
        for day, pos in enumerate(bulbs,1):
            pos -= 1
            idx = pos//K
            minBucket[idx] = min(minBucket[idx], pos)
            if idx > 0 and maxBucket[idx-1]+K == minBucket[idx]:
                return day
            maxBucket[idx] = max(maxBucket[idx], pos)
            if idx < len(minBucket)-1 and minBucket[idx+1]-K == maxBucket[idx]:
                return day
        return -1

# https://www.youtube.com/watch?v=K8Nk0AiIX4s
# bucket


# class Solution:
#     def kEmptySlots(self, bulbs: List[int], K: int) -> int:
#         n = len(bulbs)
#         flower = [-1]*n
#         for day, pos in enumerate(bulbs):
#             flower[pos-1] = day+1
#         left = 0
#         right = left + K + 1
#         res = float('inf')
#         while right < n:
#             i = left + 1
#             while i < right and flower[i] > max(flower[left], flower[right]): #all flowers between left and right should greater than both of them
#                 i += 1
#             if i == right:
#                 res = min(res, max(flower[left], flower[right]))
#             left = i
#             right = left + K + 1
        
#         if res == float('inf'):
#             return -1
        # return res

# sliding window
