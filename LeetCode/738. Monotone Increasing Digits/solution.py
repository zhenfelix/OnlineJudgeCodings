class Solution:
    def monotoneIncreasingDigits(self, s: int) -> int:
        s = str(s)
        n = len(s)
        st = []
        flag = False
        for i, ch in enumerate(s):
            if flag:
                st.append('9')
                continue
            if not st or st[-1] <= ch:
                st.append(ch)
            else:
                flag = True
                t = st[-1]
                while st and st[-1] == t:
                    st.pop()
                st.append(chr(ord(t)-1))
                while len(st) <= i:
                    st.append('9')
        return int(''.join(st))


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        arr = list(str(n))
        m = len(arr)
        pre = '0'
        flag = True
        for i, a in enumerate(arr):
            if a < pre and flag:
                flag = False
                j = i-1
                while j > 0 and arr[j-1] == arr[j]:
                    j -= 1
                arr[j] = str(int(arr[j])-1)
                # print(j,arr[j])
                j += 1
                while j < i:
                    arr[j] = '9'
                    j += 1
            if not flag:
                arr[i] = '9'
            pre = arr[i]
            print(i,a,arr)
        return int(''.join(arr))


