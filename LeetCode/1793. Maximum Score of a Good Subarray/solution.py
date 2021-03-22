class Solution:
    def maximumScore(self, A, k):
        res = mini = A[k]
        i, j, n = k, k, len(A)
        while i > 0 or j < n - 1:
            if (A[i - 1] if i else 0) < (A[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, A[i], A[j])
            res = max(res, mini * (j - i + 1))
        return res        

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = [i for i in range(n)], [i for i in range(n)]
        st = []
        for i in range(n):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if not st:
                left[i] = 0
            else:
                left[i] = st[-1] + 1
            st.append(i)
        st = []
        for i in range(n)[::-1]:
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if not st:
                right[i] = n-1
            else:
                right[i] = st[-1] - 1
            st.append(i)
        res = 0
        for i in range(n):
            if left[i] <= k <= right[i]:
                res = max(res, nums[i]*(right[i]-left[i]+1))
        return res 
