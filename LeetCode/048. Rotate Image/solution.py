class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def swap(x1,y1,x2,y2):
            matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
            return

        n = len(matrix)
        left, right = 0, n-2
        row = 0
        while left <= right:
            for col in range(left,right+1):
                swap(row,col,n-1-col,row)
                swap(n-1-col,row,n-1-row,n-1-col)
                swap(n-1-row,n-1-col,col,n-1-row)
            left += 1
            right -= 1
            row += 1
        return