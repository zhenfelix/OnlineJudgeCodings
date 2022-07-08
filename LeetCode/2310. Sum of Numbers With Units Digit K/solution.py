class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for cnt in range(1, num+1):
            if num%10 != (k*cnt)%10:
                continue
            remains = (num-k*cnt)//10
            if remains >= 0:
                return cnt  
        return -1