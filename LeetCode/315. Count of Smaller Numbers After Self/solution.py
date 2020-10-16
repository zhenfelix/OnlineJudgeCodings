# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         if not nums:
#             return []
#         n = len(nums)
#         nums = [(a,i) for i, a in enumerate(nums)]
#         tmp = [0]*n
#         # print(nums)
#         res = [0]*n

#         def merge(left,right):
#             if left == right:
#                 return
#             # print(left,right,nums)
            
#             mid = (left+right)//2
#             merge(left,mid)
#             merge(mid+1,right)
#             i, j, k = mid, right, right
#             # print(left,right,nums)
#             while i >= left or j >= mid+1:
#                 # print(i,j,k)
#                 if j < mid+1 or (i >= left and nums[i] > nums[j]):
#                     tmp[k] = nums[i]
#                     res[nums[i][-1]] += j-mid
#                     i -= 1
#                 else:
#                     tmp[k] = nums[j]
#                     j -= 1
#                 k -= 1
#             # print(left,right,nums,tmp)
#             nums[left:right+1] = [x for x in tmp[left:right+1]]
#             # print(left,right,nums)
#             return

#         merge(0,n-1)
#         # print(nums)
#         return res


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = BinaryIndexedTree(len(hashTable)), []
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i]] + 1, 1)
        return r[::-1]


