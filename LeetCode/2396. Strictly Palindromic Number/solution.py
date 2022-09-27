class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def calc(b,x):
            ans = []
            while x:
                ans.append(x%b)
                x //= b 
            return ans == ans[::-1]
        return all(calc(bb,n) for bb in range(2,n-1))


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False