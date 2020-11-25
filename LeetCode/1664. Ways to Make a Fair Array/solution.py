class Solution:
    # def waysToMakeFair(self, nums: List[int]) -> int:
    #     left, right, cnt = 0, sum(x if i&1 else -x for i,x in enumerate(nums)), 0
    #     flag = -1
    #     # print(right)
    #     for i in range(len(nums)):
    #         right -= flag*nums[i]
    #         if i > 0:
    #             left -= flag*nums[i-1]
    #         if left - right == 0:
    #             cnt += 1
    #         # print(left,right,flag)
    #         flag = -flag
    #     return cnt 
    
    def waysToMakeFair(self, A):
        s1, s2 = [0, 0], [sum(A[0::2]), sum(A[1::2])]
        res = 0
        for i, a in enumerate(A):
            s2[i % 2] -= a
            res += s1[0] + s2[1] == s1[1] + s2[0]
            s1[i % 2] += a
        return res