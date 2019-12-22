# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         # nums = [n2s(num) for num in nums]
#         res = "".join(map(lambda x: x.val, sorted(map(n2s,nums))))
#         return res if res[0] != "0" else "0"

# class n2s:
#     def __init__(self, num):
#         self.val = str(num)

#     def __lt__(self, other):
#         return self.val+other.val > other.val+self.val

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num



# Mathematical proof of correctness of sorting method
# https://leetcode.com/problems/largest-number/discuss/53195/Mathematical-proof-of-correctness-of-sorting-method