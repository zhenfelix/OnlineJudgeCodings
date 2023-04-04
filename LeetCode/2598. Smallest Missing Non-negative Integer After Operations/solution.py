class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cc = Counter([x%value for x in nums])
        for i in range(len(nums)):
            if cc[i%value] == 0:
                return i  
            cc[i%value] -= 1
        return len(nums)