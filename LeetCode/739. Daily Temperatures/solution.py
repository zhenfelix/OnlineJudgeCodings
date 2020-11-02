class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        wait, st = [0]*n, []
        for i, t in enumerate(T):
            while st and T[st[-1]] < t:
                wait[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return wait