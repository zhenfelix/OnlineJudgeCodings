class Solution:
    # def numTimesAllBlue(self, light: List[int]) -> int:
    #     n = len(light)
    #     state = [1]+[-1]*n
    #     cnt = 0
    #     for idx, i in enumerate(light):
    #         # print(state)
    #         state[i] = 0
    #         if state[i-1] == 1:
    #             while i <= n and state[i] == 0:
    #                 state[i] = 1
    #                 i += 1
    #             if i-1 == idx+1:
    #                 cnt += 1
    #     return cnt
    
    
    def numTimesAllBlue(self, A):
        right = res = 0
        for i, a in enumerate(A, 1):
            right = max(right, a)
            res += right == i
        return res