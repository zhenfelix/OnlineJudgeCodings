class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left = [0]*n 
        s = 0
        st = []
        for i in range(n):
            while st and maxHeights[st[-1]] > maxHeights[i]:
                j = st.pop()
                pj = st[-1] if st else -1
                s -= (j-pj)*(maxHeights[j]-maxHeights[i])
            st.append(i)
            s += maxHeights[i]
            left[i] = s 
        right = [0]*n 
        s = 0
        st = []
        for i in range(n)[::-1]:
            while st and maxHeights[st[-1]] > maxHeights[i]:
                j = st.pop()
                pj = st[-1] if st else n
                s -= (pj-j)*(maxHeights[j]-maxHeights[i])
            st.append(i)
            s += maxHeights[i]
            right[i] = s 
        # print(left,right)
        return max(left[i]+right[i]-maxHeights[i] for i in range(n))