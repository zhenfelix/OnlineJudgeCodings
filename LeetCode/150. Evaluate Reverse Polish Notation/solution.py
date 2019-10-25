class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in "+-/*":
                b = st.pop()
                a = st.pop()
                t = str(int(eval(a+t+b)))
            st.append(t)
        return int(st[-1])