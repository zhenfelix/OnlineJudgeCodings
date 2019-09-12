import random

# class Solution:

#     def __init__(self, nums: List[int]):
#         self.mp = {}
#         for i, num in enumerate(nums):
#             if num not in self.mp:
#                 self.mp[num] = []
#             self.mp[num].append(i)

#     def pick(self, target: int) -> int:
#         nums = self.mp[target]
#         n = len(nums)
#         idx = random.randint(0,n-1)
#         return nums[idx]

# class Solution(object):
#     def __init__(self, nums):
#         self.indexes = collections.defaultdict(list)
#         for i, num in enumerate(nums):
#             self.indexes[num].append(i)

#     def pick(self, target):
#         return random.choice(self.indexes[target])

class Solution:

    def __init__(self, nums):
        self.nums = nums
    
    def pick(self, target):
        result = -1
        count = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            else:
                if random.randint(0,count) == 0:
                    result = i
                count += 1
        
        return result



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)