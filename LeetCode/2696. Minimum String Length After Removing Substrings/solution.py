class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for ch in s:
            if st and st[-1]+ch in ["AB","CD"]:
                st.pop()
            else:
                st.append(ch)
        return len(st)