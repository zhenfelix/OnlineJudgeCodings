# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         heapq.heapify(arr)
#         res = []
#         for _ in range(k):
#             res.append(heapq.heappop(arr))
#         return res

# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         q = [-float('inf')]*k
#         for a in arr:
#             heapq.heappushpop(q,-a)
#         return [-a for a in q]


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if k == len(arr):
            return arr
        n = len(arr)
        idx = random.randint(0,n-1)
        arr[idx], arr[-1] = arr[-1], arr[idx]
        left, right = 0, n-2
        while left <= right:
            while left <= right and arr[left] <= arr[-1]:
                left += 1
            while left <= right and arr[right] > arr[-1]:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        arr[left], arr[-1] = arr[-1], arr[left]
        # if left in [k,k-1]:
        #     return arr[:k]
        # elif left < k:
        #     return arr[:left] + self.getLeastNumbers(arr[left:],k-left)
        # else:
        #     return self.getLeastNumbers(arr[:left],k)
        if left <= k:
            return arr[:left] + self.getLeastNumbers(arr[left:],k-left)
        else:
            return self.getLeastNumbers(arr[:left],k)
