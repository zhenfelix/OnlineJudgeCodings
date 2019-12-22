class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        st, sums = [(-float("inf"),-1,0)], 0
        for i, a in enumerate(A):
            while st[-1][0] > a:
                st.pop()
            val, idx, postsum = st[-1]
            postsum += a*(i-idx)
            sums += postsum
            st.append((a,i,postsum))
        return sums%(10**9+7)