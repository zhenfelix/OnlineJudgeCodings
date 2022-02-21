class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num2 > num1:
            return self.countOperations(num2,num1)
        if num2 == 0:
            return 0
        return self.countOperations(num2, num1%num2)+num1//num2