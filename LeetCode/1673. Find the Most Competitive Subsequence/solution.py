class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(nums[i],i) for i in range(n-k)]
        heapq.heapify(q)
        res = [-1]
        for i in range(n-k,n):
            heapq.heappush(q, (nums[i],i))
            while q:
                val, idx = heapq.heappop(q)
                if idx > res[-1]:
                    res.append(idx)
                    break
        return [nums[i] for i in res][1:]





```python
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        n = len(nums)
        for i, cur in enumerate(nums):
            while st and len(st)+n-i > k and st[-1] > cur:
                st.pop()
            st.append(cur)
        return st[:k] 
```

假设最优解的子序列是...a_i,a_j... 其中原来序列中的a_i和a_j在最优子序列中相邻，那么如果a_i>a_j并且a_j后的子序列并未完全填充，那么我们总可以用a_j替代a_i,并从a_j后边再补充一个维持总数不变，但是子序列的字典减少了，所以推出矛盾。注意边界条件，当a_j在子序列的首位的时候，它一定是可行范围内最小的，所以我们可以推出贪心策略，在构造子序列的过程中，只要子序列中的a_i比当前的a_j大，并且len(st)+n-j > k那么就可以取而代之
    
    
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




class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        res = []
        for i, cur in enumerate(nums):
            while q and q[-1] > cur:
                q.pop()
            q.append(cur)
            if i == n-k:
                res.append(q.popleft())
                k -= 1
        return res 