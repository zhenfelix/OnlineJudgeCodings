class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        st = []
        n = len(heights)
        ans = [0]*n 
        for i in range(n)[::-1]:
            cnt = 0
            while st and heights[i] > st[-1]:
                cnt += 1
                st.pop()
            if st:
                cnt += 1
            ans[i] = cnt 
            st.append(heights[i])
            
        return ans