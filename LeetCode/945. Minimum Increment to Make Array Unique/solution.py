class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        res, cur, n = 0, min(A), len(A)
        heapq.heapify(A)
        while A:
            if cur >= A[0]:
                res += cur - heapq.heappop(A)
            cur += 1
        return res

            

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        res, cur, n = 0, -1, len(A)
        heapq.heapify(A)
        while A:
            cur = max(cur+1,A[0])
            res += cur - heapq.heappop(A)
        return res

            

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        res, cur = 0, -1
        for a in sorted(A):
            cur = max(cur+1,a)
            res += cur - a
        return res

    # def minIncrementForUnique(self, A):
    #     c = collections.Counter(A)
    #     res = need = 0
    #     for x in sorted(c):
    #         res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
    #         need = max(need, x) + c[x]
    #     return res


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        res, reach = 0, {}
        def find(x):
            reach[x] = find(reach[x]+1) if x in reach else x
            return reach[x]
        return sum(find(a)-a for a in A)