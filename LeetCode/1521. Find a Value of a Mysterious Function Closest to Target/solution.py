class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = float('inf')
        cur = []
        for a in arr:
            nxt = [a]
            for b in cur:
                b &= a 
                if b < nxt[-1]:
                    nxt.append(b)
            for b in nxt:
                ans = min(ans, abs(target-b))
            cur = nxt
        return ans 


# class Solution:
#     def closestToTarget(self, arr: List[int], target: int) -> int:
#         ans = float('inf')
#         for i in range(0, len(arr)):
#             aux = arr[i]
#             for j in range(i, len(arr)):
#                 aux= aux&arr[j]
#                 ans = min(ans, abs(aux-target))
#                 if ans==0: return ans
#                 if aux<=target: break
#             if aux>target:break
#         return ans


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        prefix, res = set(), float('inf')
        for a in arr:
            tmp = {p&a for p in prefix}
            tmp.add(a)
            for p in tmp:
                res = min(abs(p-target),res)
            prefix = tmp
        return res

