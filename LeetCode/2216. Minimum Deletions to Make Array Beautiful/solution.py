class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        st, cnt = [], 0
        while nums:
            x = nums.pop()
            if not st:
                st.append(x)
            elif st[-1] == x:
                cnt += 1
            else:
                st.pop()
        return cnt+len(st)