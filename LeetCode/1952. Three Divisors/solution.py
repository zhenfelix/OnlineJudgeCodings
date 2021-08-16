class Solution:
    def isThree(self, n: int) -> bool:
        flag, cur = False, 2
        while cur*cur <= n:
            if n%cur == 0:
                if cur*cur == n:
                    flag = True
                else:
                    return False
            cur += 1
        return flag