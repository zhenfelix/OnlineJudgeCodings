class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def func(x):
            cnt = 0
            while x != 1:
                cnt += 1
                if x&1:
                    x = x*3+1
                else:
                    x //= 2
            return cnt
        arr = [i for i in range(lo,hi+1)]
        arr.sort(key=lambda x: (func(x),x))
        return arr[k-1]
                