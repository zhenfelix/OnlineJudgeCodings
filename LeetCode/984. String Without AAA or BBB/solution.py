class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        A = "ab"
        B = "ba"
        idx = 0
        if a < b:
            a, b = b, a 
            idx = 1
        n = (a+1)//2
        arr = [[] for _ in range(n)]
        for i in range(n*2):
            if a <= 0:
                break
            arr[i%n].append(A[idx])
            a -= 1
        for i in range(n*2):
            if b <= 0:
                break
            arr[i%n].append(B[idx])
            b -= 1
        ans = []
        for tmp in arr:
            for ch in tmp:
                ans.append(ch)
        return ''.join(ans)


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        arr = [(a,'a'),(b,'b')]
        res = ""
        for _ in range(a+b):
            arr.sort(key=lambda x: -x[0])
            for i, (cnt,ch) in enumerate(arr):
                if res[-2:] != ch+ch:
                    res += ch
                    arr[i] = (cnt-1,ch)
                    break
        return res