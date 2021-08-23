class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt = 0
        arr = []
        for line in matrix:
            for x in line:
                if x < 0:
                    cnt += 1
                arr.append(x)
        if cnt%2 == 0:
            return sum(abs(x) for x in arr)
        arr.sort(key = lambda x: abs(x))
        return -abs(arr[0]) + sum(abs(x) for x in arr[1:])