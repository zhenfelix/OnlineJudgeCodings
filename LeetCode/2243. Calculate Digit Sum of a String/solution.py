class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def calc(x):
            return sum(ord(y)-ord('0') for y in x)
        while len(s) > k:
            arr = [calc(s[i:i+k]) for i in range(0,len(s),k)]
            s = ''.join(map(str,arr))
        return s
