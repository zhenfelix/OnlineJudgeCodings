class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        idx = [0]*n
        cur_max, cur_min = 0, float('inf')
        for row, col in enumerate(idx):
            cur_max = max(cur_max, mat[row][col])
            # cur_min = min(cur_min, mat[row][col])
        while True:
            cnt = 0
            cur_max_tmp = 0
            for row, col in enumerate(idx):
                while mat[row][idx[row]] < cur_max:
                    idx[row] += 1
                    if idx[row] == m:
                        return -1
                if mat[row][idx[row]] == cur_max:
                    cnt += 1
                cur_max_tmp = max(cur_max_tmp, mat[row][idx[row]])
            if cnt == n:
                return cur_max
            cur_max = cur_max_tmp
        return -1
                    

# class Solution:
#     def smallestCommonElement(self, mat: List[List[int]]) -> int:
#         s=set(mat[0])
#         for i in range(1,len(mat)):
#             s = s.intersection(mat[i])
#         if s:
#             return min(s)
#         else:
#             return -1