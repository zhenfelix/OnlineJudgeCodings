class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def check(cha, chb, cx, cy):
            st = []
            ans = 0
            for ch in s+'$':
                if ch != cha and ch != chb:
                    n = len(st)
                    left, right = 0, n-1
                    while left < right:
                        if st[left] != st[right]:
                            ans += cy
                        left += 1
                        right -= 1
                    st = []
                elif st and st[-1] == cha and ch == chb:
                    st.pop()
                    ans += cx
                else:
                    st.append(ch)
            return ans 
        if x > y:
            return check('a','b', x, y)
        else:
            return check('b', 'a', y, x)



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