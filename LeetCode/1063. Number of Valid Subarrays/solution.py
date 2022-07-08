class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(-1)
        st = []
        st.append(n)
        ans = 0
        for i in range(n)[::-1]:
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            ans += st[-1]-i
            st.append(i)
        return ans