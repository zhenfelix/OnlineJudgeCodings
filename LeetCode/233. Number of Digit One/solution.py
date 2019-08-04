class Solution:
    def countDigitOne(self, n: int) -> int:
        d, ans = 1, 0
        tmp = n//d
        while tmp > 0:
            x = tmp%10
            left = tmp//10
            right = n - (tmp*d)
            # print(left, right)
            ans += left*d
            if x == 1:
                ans += right+1
            elif x > 1:
                ans += d
            d *= 10
            tmp = n//d
        return ans

## find counts of 1 on digit x
