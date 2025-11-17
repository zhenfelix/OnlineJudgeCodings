class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        st = []
        ans = 0
        for i in range(n):
            mx = 0
            while st and nums[st[-1]] < nums[i]:
                j = st.pop()
                if nums[j] > mx and i-j > 1:
                    # print(j,i)
                    ans += 1
                mx = max(mx,nums[j])
            if st and nums[st[-1]] > mx and i-st[-1] > 1:
                ans += 1
            st.append(i)
        return ans 