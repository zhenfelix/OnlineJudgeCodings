class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sums = 0
        nums.append(float('inf'))
        st = [-1]
        for i, v in enumerate(nums):
            while nums[st[-1]] < v:
                j = st.pop()
                sums += (j-st[-1])*(i-j)*nums[j]
            st.append(i)
        nums[-1] = -float('inf')
        st = [-1]
        for i, v in enumerate(nums):
            while nums[st[-1]] > v:
                j = st.pop()
                sums -= (j-st[-1])*(i-j)*nums[j]
            st.append(i)
        return sums

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sums = 0
        n = len(nums)
        for i in range(n):
            lo, hi = float('inf'), -float('inf')
            for j in range(i,n):
                lo = min(lo, nums[j])
                hi = max(hi, nums[j])
                sums += hi-lo
        return sums