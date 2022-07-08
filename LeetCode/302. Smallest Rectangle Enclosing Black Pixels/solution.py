class Solution:
    def minArea(self, image: List[List[str]], r: int, c: int) -> int:
        n, m = len(image), len(image[0])
        def isblack(scan_col, j, limit):
            for i in range(limit):
                if scan_col:
                    if image[i][j] == '1':
                        return 1
                else:
                    if image[j][i] == '1':
                        return 1
            return 0

        def bs(lo,hi,white_lo,scan_col,limit):
            # print("before: ",white_lo,scan_col,limit,lo,hi)
            while lo <= hi:
                mid = (lo+hi)//2
                if isblack(scan_col,mid,limit)^white_lo:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # print("after: ","white_lo: ",white_lo,"scan_col: ",scan_col,limit,lo,hi)
            if white_lo:
                return lo 
            else:
                return hi 

        return (bs(c,m-1,0,1,n)-bs(0,c,1,1,n)+1)*(bs(r,n-1,0,0,m)-bs(0,r,1,0,m)+1)



# from collections import deque

# class Solution:
#     def minArea(self, image: List[List[str]], x: int, y: int) -> int:
#         n = len(image)
#         m = len(image[0])
#         left, right, up, down = y, y, x, x
#         q = deque()
#         visited = set()
#         q.append((x,y))
#         while q:
#             front = q.popleft()
#             left = min(left, front[1])
#             right = max(right, front[1])
#             up = min(up, front[0])
#             down = max(down, front[0])
#             for delta in [(0,1),(0,-1),(1,0),(-1,0)]:
#                 row, col = front[0]+delta[0], front[1]+delta[1]
#                 if (row,col) not in visited and 0 <= row < n and 0 <= col < m and image[row][col] == '1':
#                     visited.add((row,col))
#                     q.append((row,col))
#         return (right-left+1)*(down-up+1)


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        n = len(image)
        m = len(image[0])
        def row_search(lo,hi,row_lo,row_hi,black):
            def findOne(col):
                for r in range(row_lo,row_hi+1):
                    if image[r][col] == '1':
                        return True
                return False

            while lo <= hi:
                mid = (lo+hi)//2
                if findOne(mid) ^ black:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        def col_search(lo,hi,col_lo,col_hi,black):
            def findOne(row):
                for c in range(col_lo,col_hi+1):
                    if image[row][c] == '1':
                        return True
                return False
            while lo <= hi:
                mid = (lo+hi)//2
                if findOne(mid) ^ black:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        left = row_search(0,y,0,n-1,True)
        right = row_search(y,m-1,0,n-1,False)
        up = col_search(0,x,left,right-1,True)
        down = col_search(x,n-1,left,right-1,False)
        return (down-up)*(right-left)