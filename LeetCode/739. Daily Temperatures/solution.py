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


inf = math.inf
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n 
        temperatures.append(inf)
        st = [-1]
        for i in range(n):
            while temperatures[st[-1]] < temperatures[i]:
                ans[st[-1]] = i-st[-1]
                st.pop()
            st.append(i)
        return ans
