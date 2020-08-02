class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        start, end = {}, {}
        for i, ch in enumerate(s):
            if ch not in start:
                start[ch] = i 
            end[ch] = i
        st, res = [], []
        for i, ch in enumerate(s):
            if start[ch] == i:
                st.append(i)
            if end[ch] == i and st:
                pre = s[st.pop()]
                
                for k in range(start[pre],end[ch]+1):
                    if start[s[k]] < start[pre] or end[s[k]] > end[ch]:
                        break
                else:
                    res.append(s[start[pre]:end[ch]+1])
                    st = []
        return res