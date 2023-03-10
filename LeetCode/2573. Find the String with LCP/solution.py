# class Solution:
#     def findTheString(self, lcp: List[List[int]]) -> str:
#         n = len(lcp)
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     if lcp[i][j] != n-i:
#                         return ""
#                 if lcp[i][j] != lcp[j][i]:
#                     return ""
#                 if lcp[i][j] > n-max(i,j):
#                     return ""
#                 if i < j and i+1 < n and j+1 < n:
#                     # if lcp[i][j] == 0 and lcp[i+1][j+1] != 0:
#                     #     return ""
#                     if lcp[i][j] > 0 and lcp[i][j] != lcp[i+1][j+1]+1:
#                         return ""
#         ans = [] 
#         for i in range(n):
#             for ch in string.ascii_lowercase:
#                 flag = True
#                 for j in range(i):
#                     if ch == ans[j]:
#                         if lcp[i][j] == 0:
#                             flag = False
#                             break
#                     else:
#                         if lcp[i][j] > 0:
#                             flag = False
#                             break 
#                 if flag:
#                     ans.append(ch)
#                     break
#             if len(ans) < i+1:
#                 return ""
#         return ''.join(ans)


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ans = ['' for _ in range(n)]
        char = 'a'
        for i in range(n):
            if ans[i] == '':
                if char > 'z': return ''
                ans[i] = char
                for j in range(n):
                    if lcp[i][j]:
                        ans[j] = ans[i]
                char = chr(ord(char) + 1)
        for i in range(n):
            if lcp[i][n-1] != (ans[i] == ans[n-1]): return ''
            if lcp[n-1][i] != (ans[i] == ans[n-1]): return ''
        for i in range(n-1):
            for j in range(n-1):
                if ans[i] == ans[j]:
                    if lcp[i][j] != lcp[i+1][j+1] + 1: return ''
                else:
                    if lcp[i][j] != 0: return ''
        return ''.join(ans)


# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/JB73eh/view/Px34pu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。