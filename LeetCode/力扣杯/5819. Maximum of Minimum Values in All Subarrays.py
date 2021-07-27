class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.append(-1)
        left = [i for i in range(n)]
        right = [i for i in range(n)]
        st = [-1]
        for i in range(n):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            left[i] = st[-1]+1
            st.append(i)
        st = [n]
        for i in range(n)[::-1]:
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            right[i] = st[-1]-1
            st.append(i)
        dp = [0]*n 
        # print(left,right)
        for i in range(n):
            sz = right[i]-left[i]
            dp[sz] = max(dp[sz], nums[i])
        for i in range(n-1)[::-1]:
            dp[i] = max(dp[i], dp[i+1])

        return dp