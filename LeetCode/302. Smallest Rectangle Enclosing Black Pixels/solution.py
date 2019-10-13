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