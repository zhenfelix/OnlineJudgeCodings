class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s: 
            if stack and abs(ord(stack[-1]) - ord(c)) == 32: stack.pop() #pop "bad"
            else: stack.append(c) #push "good"
        return "".join(stack)


class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for ch in s:
            st.append(ch)
            while len(st) > 1 and st[-2].lower() == st[-1].lower() and st[-2] != st[-1]:
                st.pop()
                st.pop()
        return ''.join(st)