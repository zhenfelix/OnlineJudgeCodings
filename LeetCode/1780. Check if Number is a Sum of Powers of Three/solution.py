class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 0:
            return True
        if n%3 > 1:
            return False
        n -= (n%3)
        return self.checkPowersOfThree(n//3)


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            else:
                n //= 3
        return True      