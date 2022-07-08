class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        pre, ans = 0, 0
        for u, r in brackets:
            if u < income:
                ans += (u-pre)*r/100
                pre = u
            else:
                ans += (income-pre)*r/100
                break
        return ans