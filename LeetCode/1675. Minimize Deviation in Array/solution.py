class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = [-x*2 if x&1 else -x for x in nums]
        heapify(nums)
        mi = -max(nums)
        ans = inf 
        while True:
            # print(nums,mi)
            x = -heappop(nums)
            ans = min(ans, x-mi)
            if x&1: break
            x //= 2  
            mi = min(mi, x)
            heappush(nums, -x)
        return ans 


class Solution:
    # def minimumDeviation(self, nums: List[int]) -> int:
    #     remove = Counter()
    #     nums = [x*2 if x&1 else x for x in nums]
    #     mi = nums[:]
    #     mx = [-x for x in nums]
    #     heapq.heapify(mi)
    #     heapq.heapify(mx)
    #     res = float('inf')
    #     while (-mx[0])&1 == 0:
    #         res = min(res, -mx[0]-mi[0])
    #         cur = -heapq.heappop(mx)
    #         remove[cur] += 1
    #         heapq.heappush(mx,-cur//2)
    #         while mi and remove[mi[0]] > 0:
    #             remove[mi[0]] -= 1
    #             heapq.heappop(mi)
    #         heapq.heappush(mi,cur//2)
    #     res = min(res, -mx[0]-mi[0])
    #     return res 

    def minimumDeviation(self, A):
        pq = []
        for a in A:
            heapq.heappush(pq, -a * 2 if a % 2 else -a)
        res = float('inf')
        mi = -max(pq)
        while True:
            a = -heapq.heappop(pq)
            res = min(res, a - mi)
            if a&1:
                break
            mi = min(mi, a // 2)
            heapq.heappush(pq, -a // 2)
        return res


class Solution:
    def minimumDeviation(self, A):
        pq = []
        for a in A:
            heapq.heappush(pq, [a // (a & -a), a])
        res = float('inf')
        ma = max(a for a, a0 in pq)
        while len(pq) == len(A):
            a, a0 = heapq.heappop(pq)
            res = min(res, ma - a)
            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heapq.heappush(pq, [a * 2, a0])
        return res