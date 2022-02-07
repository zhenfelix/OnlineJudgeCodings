class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        left = [sum(nums[:n])]
        q = [-x for x in nums[:n]]
        heapq.heapify(q)
        for i in range(n):
            heapq.heappush(q,-nums[n+i])
            left.append(left[-1]+heapq.heappop(q)+nums[n+i])
        right = [sum(nums[-n:])]
        q = [x for x in nums[-n:]]
        heapq.heapify(q)
        for i in range(n):
            heapq.heappush(q,nums[2*n-1-i])
            right.append(right[-1]-heapq.heappop(q)+nums[2*n-1-i])
        return min(l-r for l, r in zip(left,right[::-1]))