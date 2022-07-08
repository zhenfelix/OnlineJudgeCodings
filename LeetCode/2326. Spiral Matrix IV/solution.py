# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, n: int, m: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*m for _ in range(n)]
        drc = [(0,1),(1,0),(0,-1),(-1,0)]
        r, c, idx = 0, 0, 0
        def valid(x,y):
            return 0 <= x < n and 0 <= y < m and mat[x][y] == -1

        while head:
            mat[r][c] = head.val 
            head = head.next
            while head:
                dr, dc = drc[idx]
                dr += r 
                dc += c 
                if valid(dr,dc):
                    r, c = dr, dc 
                    break
                idx = (idx+1)%4
        return mat



# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def spiralMatrix(self, n: int, m: int, head: Optional[ListNode]) -> List[List[int]]:
#         mat = [[-1]*m for _ in range(n)]
#         r, c = 0, 0
#         def valid(x,y):
#             return 0 <= x < n and 0 <= y < m and mat[x][y] == -1

#         while head:
#             while head and valid(r,c):
#                 mat[r][c] = head.val  
#                 head = head.next
#                 c += 1
#             c -= 1
#             r += 1
#             while head and valid(r,c):
#                 mat[r][c] = head.val 
#                 head = head.next
#                 r += 1
#             r -= 1
#             c -= 1
#             while head and valid(r,c):
#                 mat[r][c] = head.val 
#                 head = head.next
#                 c -= 1
#             c += 1
#             r -= 1
#             while head and valid(r,c):
#                 mat[r][c] = head.val 
#                 head = head.next
#                 r -= 1
#             r += 1
#             c += 1
#         return mat