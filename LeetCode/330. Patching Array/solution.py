# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:
#         def transform(cur, left, shift):
#             new_cur = cur.copy()
#             first = n
#             for i in range(n-1, left-1, -1):
#                 if i-shift >= 0 and new_cur[i-shift]:
#                     new_cur[i] = True
#                 if not new_cur[i]:
#                     first = i 
#             return new_cur, first

#         start_, left_ = [False]*n, 0
#         for num in nums:
#             start_, left_ = transform(start_, left_, num)
#             if num-1 < n:
#                 start_[num-1] = True
#             while left_ < n and start_[left_]:
#                 left_ += 1
#         # print(start_)
#         cc = 0
#         ans_start_, ans_left_ = [False]*n, -1
#         while True:
#             if left_ == n:
#                 return cc

#             for sft in range(1,left_+2):
#                 new_start_, new_left_ = transform(start_, left_, sft)
#                 if sft-1 < n:
#                     new_start_[sft-1] = True
#                 while new_left_ < n and new_start_[new_left_]:
#                     new_left_ += 1
                    
#                 if new_left_ > ans_left_:
#                     ans_start_, ans_left_ = new_start_.copy(), new_left_

#             start_, left_ = ans_start_.copy(), ans_left_ 
#             # print(start_)
#             # print(left_)
#             cc += 1

#         return -1

# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:
#         left, idx, cc = 1, 0, 0
#         while left <= n:
#             if idx < len(nums) and nums[idx] <= left:
#                 left += nums[idx]
#                 idx += 1
#             else:
#                 left += left
#                 cc += 1
#         return cc

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach, m, idx = 0, len(nums), 0
        res = 0
        while reach < n:
            if nums[idx] > reach + 1:
                res += 1
                reach += reach + 1
            else:
                reach += nums[idx]
                idx += 1
        return res