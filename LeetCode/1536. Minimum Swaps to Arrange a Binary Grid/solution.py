class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        arr, n = [], len(grid)
        for i in range(n):
            cnt, j = 0, n-1
            while j >= 0 and grid[i][j] == 0:
                cnt += 1
                j -= 1
            arr.append(cnt)
        # print(arr)
        used = set()
        res = 0
        for i in range(n):
            cnt = 0
            for j in range(n):
                if j in used:
                    continue
                if arr[j] >= n-1-i:
                    used.add(j)
                    break
                cnt += 1
            else:
                return -1
            res += cnt


        return res
