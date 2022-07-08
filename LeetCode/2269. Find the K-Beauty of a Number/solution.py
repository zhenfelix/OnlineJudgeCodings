class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        cnt = 0
        n = len(num)
        a = int(num)
        for i in range(n-k+1):
            b = int(num[i:i+k])
            if b > 0 and a%b == 0:
                cnt += 1
        return cnt