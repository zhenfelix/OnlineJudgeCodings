class Solution:
    # def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    #     n = len(nums)
    #     res = []
    #     for r in range(n):
    #         for c in range(len(nums[r])):
    #             res.append((r+c,c,nums[r][c]))
    #     return list(map(lambda x:x[-1], sorted(res)))
    
    def findDiagonalOrder(self, A):
        res = []
        for i, r in enumerate(A):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)
        return [a for r in res for a in reversed(r)]


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        m = len(nums)
        
        queue = collections.deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])
            # we only add the number at the bottom if we are at column 0
            if col == 0 and row + 1 < m:
                queue.append((row + 1, col))
            # add the number on the right
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
            
        return ans