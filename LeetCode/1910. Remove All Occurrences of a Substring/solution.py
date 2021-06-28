class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []
        cur = s 
        m = len(part)
        while cur:
            idx = cur.find(part)
            if idx == -1:
                break
            cur = cur[:idx] + cur[idx+m:]
        return cur

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n, m = len(s), len(part)
        nxt = [-1]*m
        i, j = 0, -1
        while i < m-1:
            if part[i+1] != part[j+1] and j != -1:
                j = nxt[j]
            else:
                if part[i+1] == part[j+1]:
                    j += 1
                i += 1
                nxt[i] = j
        i, j = -1, -1
        st, res = [-1], []
        while i < n-1:
            if s[i+1] != part[j+1] and j != -1:
                j = nxt[j]
            else:
                if s[i+1] == part[j+1]:
                    j += 1
                i += 1
                res.append(s[i])
                st.append(j)
                if j == m-1:
                    st = st[:-m]
                    res = res[:-m]
                    j = st[-1]
        return ''.join(res)
