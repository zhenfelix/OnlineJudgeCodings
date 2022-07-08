class Solution:
    def buildTransferStation(self, area: List[List[int]]) -> int:
        n, m = len(area), len(area[0])
        rowsum = [0]*n 
        colsum = [0]*m 
        for i in range(n):
            rowsum[i] = sum(area[i][j] for j in range(m))
        for j in range(m):
            colsum[j] = sum(area[i][j] for i in range(n))
        ans = 0
        def calc(arr):
            sz = len(arr)
            left, right = [0]*sz, [0]*sz
            cnt = 0
            for i in range(sz):
                left[i] = left[i-1]+cnt
                cnt += arr[i]
            cnt = 0
            for i in range(sz)[::-1]:
                right[i] = right[(i+1)%sz]+cnt
                cnt += arr[i]
            ans = float('inf')
            for i in range(sz):
                ans = min(ans, left[i]+right[i])
            return ans 
        return calc(rowsum)+calc(colsum)

