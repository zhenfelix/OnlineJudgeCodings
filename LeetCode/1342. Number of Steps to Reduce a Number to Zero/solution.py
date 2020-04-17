class Solution:
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num:
            # print(num,num&1)
            step += 1+(num&1)
            num >>= 1
        return step-1