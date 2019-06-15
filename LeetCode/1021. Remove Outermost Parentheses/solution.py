class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ""
        n = len(S)
        st = []
        start = 0
        for i in range(n):
            if len(st)>0:
                if st[-1] == '(' and S[i] == ')':
                    st.pop()
                else:
                    st.append(S[i])
            else:
                st.append(S[i])
                
            if len(st) == 0:
                ans = ans+S[start+1:i]
                start = i+1
        
        return ans
                