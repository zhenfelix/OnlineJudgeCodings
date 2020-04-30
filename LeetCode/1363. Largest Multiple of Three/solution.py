class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        n = len(digits)
        digits.sort()
        dp = defaultdict(list)
        r = 0
        for i in range(n)[::-1]:
            dp[digits[i]%3].append(digits[i])
            r += digits[i]
            r %= 3
        dp[1].sort()
        dp[2].sort()
        to_remove = []
        if r:
            if len(dp[r]) >= 1:
                to_remove += [dp[r][0]]
            elif len(dp[3-r]) >= 2:
                to_remove += dp[3-r][:2]
            else:
                return ""
        digits_ = digits[:]
        digits = []
        # print(to_remove,r)
        for ch in digits_[::-1]:
            if to_remove and ch == to_remove[-1]:
                to_remove.pop()
                continue
            digits += [ch]
        if digits and digits[0] == 0:
            return '0'
        return ''.join(map(str,digits))
            
