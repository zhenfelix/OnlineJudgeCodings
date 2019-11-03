# class Solution:
#     def findMinMoves(self, machines):
#         total, n = sum(machines), len(machines)
#         if total % n: return -1
#         target, res, toRight = total // n, 0, 0
#         for m in machines:
#             toRight = m + toRight - target
#             # res = max(res, abs(toRight), abs(m - target))
#             res = max(res, abs(toRight), m - target)
#         return res

class Solution:
    def findMinMoves(self, machines):
        total, n = sum(machines), len(machines)
        if total % n: return -1
        target, res, right, left = total // n, 0, total, 0
        for i in range(n):
            cur, left, right = machines[i], (0 if i==0 else left+machines[i-1]), right-machines[i]
            # print(i,left,cur,right)
            res = max(res,max(0,-(left-target*i)), max(0,cur-target), max(0,-(right-target*(n-1-i))))
            # print(res)
        return res