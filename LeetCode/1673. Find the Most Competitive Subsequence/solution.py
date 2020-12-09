# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         q, res = deque(), []
#         n = len(nums)
#         for i, cur in enumerate(nums):
#             while q and q[-1] > cur:
#                 q.pop()
#             q.append(cur)
#             if n - i <= k:
#                 res.append(q.popleft())
#         return res 



class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        n = len(nums)
        for i, cur in enumerate(nums):
            while st and len(st) > k-n+i and st[-1] > cur:
                st.pop()
            st.append(cur)
        return st[:k] 
    
    
# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         q = [(nums[i],i) for i in range(n-k)]
#         heapq.heapify(q)
#         res = [-1]
#         for i in range(n-k,n):
#             heapq.heappush(q, (nums[i],i))
#             while q:
#                 val, idx = heapq.heappop(q)
#                 if idx > res[-1]:
#                     res.append(idx)
#                     break
#         return [nums[i] for i in res][1:]
