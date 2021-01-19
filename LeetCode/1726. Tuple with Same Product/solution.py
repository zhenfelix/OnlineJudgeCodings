class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cc = Counter()
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                mul = nums[i]*nums[j]
                res += 8*cc[mul]
                cc[mul] += 1
        return res 