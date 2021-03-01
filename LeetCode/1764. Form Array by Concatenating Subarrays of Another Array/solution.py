class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        def find(pattern, idx):
            m = len(pattern)
            while idx+m <= len(nums) and pattern != nums[idx:idx+m]:
                idx += 1
            return idx+m if idx+m <= len(nums) else -1

        cur = 0
        for g in groups:
            cur = find(g,cur)
            if cur < 0:
                return False
        return True


# class Solution:
#     def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
#         i = 0
#         for grp in groups: 
#             for ii in range(i, len(nums)):
#                 if nums[ii:ii+len(grp)] == grp: 
#                     i = ii + len(grp)
#                     break 
#             else: return False
#         return True


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for group in groups:
            failure = [0] * len(group)
            j = 0
            for k in range(1, len(group)):
                while j > 0 and group[j] != group[k]:
                    j = failure[j-1]
                j += group[j] == group[k]
                failure[k] = j
            j = 0
            for k in range(i, len(nums)):
                while j > 0 and group[j] != nums[k]:
                    j = failure[j-1]
                j += group[j] == nums[k]
                if j == len(group):
                    i = k + 1
                    break
            else:
                return False
        return True