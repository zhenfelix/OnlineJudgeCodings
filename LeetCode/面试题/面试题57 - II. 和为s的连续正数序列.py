# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         cnt, target = 2, 2*target
#         res = []
#         while cnt*cnt <= target:
#             if target%cnt == 0:
#                 lo = target//cnt+1-cnt
#                 if lo%2 == 0:
#                     lo //= 2
#                     res.append([i for i in range(lo,lo+cnt)])
#             cnt += 1
#         return res[::-1]

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right, sums = 1, 0, 0
        res = []
        while right < target:
        	if sums == target:
        		res.append([i for i in range(left,right+1)])
        		right += 1
        		sums += right
        	elif sums < target:
        		right += 1
        		sums += right
        	else:
        		sums -= left
        		left += 1
        return res