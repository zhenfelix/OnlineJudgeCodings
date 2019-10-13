# class Solution:
#     def findPermutation(self, s: str) -> List[int]:
#         n = len(s) + 1
#         ans = [None]
        
        
#         def dfs(path, res):
#             # print(path)
#             if len(path) == n:
#                 res[0] = path
#                 # print('found',path)
#                 return True
#             flag = s[len(path)-1]
#             if flag == 'I':
#                 for nxt in range(path[-1]+1,n+1):
#                     if nxt not in path and dfs(path+[nxt],res):
#                         return True
#             else:
#                 for nxt in range(1,path[-1]):
#                     if nxt not in path and dfs(path+[nxt],res):
#                         return True
#             return False

        
#         for i in range(1,n+1):
#             if dfs([i],ans):
#                 return ans[0]
#         return ans[0]


# class Solution:
#     def findPermutation(self, s: str) -> List[int]:
#         I, D = [1], []
#         pre = 'I'
#         for ch in s:
#             if ch == 'I':
#                 if D:
#                     base = D[-1]
#                 else:
#                     base = I[-1]
#                 while D:
#                     I.append(D.pop())
#                 I.append(base+1)
#                 pre = 'I'
#             else:
#                 if pre == 'I':
#                     pre = None
#                     D.append(I.pop())
#                 D.append(D[-1]+1)
#         while D:
#             I.append(D.pop())
#         return I


# class Solution:
#     def findPermutation(self, s: str) -> List[int]:
#         I, D = [1], []
#         n = len(s)
#         idx = 0
#         cur = 1
#         while idx < n:
#             while idx < n and s[idx] == 'I':
#                 I.append(cur+1)
#                 cur += 1
#                 idx += 1
#             D.append(I.pop())
#             while idx < n and s[idx] == 'D':
#                 D.append(cur+1)
#                 cur += 1
#                 idx += 1
#             while D:
#                 I.append(D.pop())
#         return I 


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        I, D = [1], []
        n = len(s)
        res = list(range(1,n+2))
        left, right = 0, 0
        i = 0
        while i < n:
            while i < n and s[i] == 'I':
                left += 1
                right += 1
                i += 1
            while i < n and s[i] == 'D':
                right += 1
                i += 1
            # print(left,right)
            res[left:right+1] = res[left:right+1][::-1]
            left = right
            # print(res)

        return res




