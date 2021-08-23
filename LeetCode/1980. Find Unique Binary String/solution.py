class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join(['1' if num[i]=='0' else '0' for i,num in enumerate(nums)])


# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         n = len(nums)
#         def convert(s):
#             x = 0
#             for ch in s:
#                 x = (x<<1)
#                 x += int(ch)
#             return x 

#         def revert(x):
#             s = []
#             for i in range(n):
#                 if (x>>i)&1:
#                     s.append('1')
#                 else:
#                     s.append('0')
#             return ''.join(s[::-1])


#         visited = set()
#         for a in nums:
#             visited.add(convert(a))
#         for i in range((1<<n)):
#             if i not in visited:
#                 return revert(i)
#         return ''