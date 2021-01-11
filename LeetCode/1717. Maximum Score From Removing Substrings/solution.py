class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def ab(arr):
            st = []
            cnt = 0
            for ch in arr:
                if ch == 'b' and st and st[-1] == 'a':
                    st.pop()
                    cnt += x 
                else:
                    st.append(ch)
            return cnt, st 
        def ba(arr):
            st = []
            cnt = 0
            for ch in arr:
                if ch == 'a' and st and st[-1] == 'b':
                    st.pop()
                    cnt += y
                else:
                    st.append(ch)
            return cnt, st 
        res = 0
        if x > y:
            delta, tmp = ab(list(s))
            res += delta
            delta, tmp = ba(tmp)
            res += delta
        else:
            delta, tmp = ba(list(s))
            res += delta
            delta, tmp = ab(tmp)
            res += delta
        return res 