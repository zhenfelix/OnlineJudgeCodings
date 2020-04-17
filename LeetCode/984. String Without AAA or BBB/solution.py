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