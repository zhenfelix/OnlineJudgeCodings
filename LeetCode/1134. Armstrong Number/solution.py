class Solution:
    def isArmstrong(self, N: int) -> bool:
        arr = []
        a = N
        while a > 0:
            arr.append(a%10)
            a //= 10
        n = len(arr)
        # print(arr)
        ans = 0
        for a in arr:
            ans += a**n
        return ans == N
        