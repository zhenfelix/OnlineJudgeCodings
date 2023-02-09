K = 2

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n 
        sts = [[] for _ in range(K)]
        tmp = []
        for i in range(n):
            v = nums[i]
            for k in range(K)[::-1]:
                while sts[k] and nums[sts[k][-1]] < v:
                    j = sts[k].pop()
                    if k == K-1:
                        ans[j] = v
                    else:
                        tmp.append(j)
                if k < K-1:
                    while tmp:
                        sts[k+1].append(tmp.pop())
            sts[0].append(i)
            
        return ans 

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n 
        q1, q2 = [], []
        for i in range(n):
            v = nums[i]
            while q2 and q2[0][0] < v:
                x, j = heappop(q2)
                ans[j] = v 
            while q1 and q1[0][0] < v:
                x, j = heappop(q1)
                heappush(q2,(x,j))
            heappush(q1,(v,i))
        return ans 

from sortedcontainers import SortedList

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n 
        arr = []
        for i, v in enumerate(nums):
            arr.append((-v,i))
        arr.sort()
        sl = SortedList()
        for v, i in arr:
            j = sl.bisect_left(i)
            if j+1 < len(sl):
                ans[i] = nums[sl[j+1]]
            sl.add(i)
        return ans 