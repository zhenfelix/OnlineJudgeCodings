# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
#         folder = sorted(folder)
#         res = []
#         mp = set()
#         for f in folder:
#             paths = f.split('/')
#             # print(paths)
#             cur = ""
#             for path in paths[1:]:
#                 cur += '/'+path
#                 if cur in mp:
#                     break
#             if cur in mp:
#                 continue
#             mp.add(f)
#             res.append(f)
#         return res

class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort()
        stack = [folder[0]]
        for f in folder[1:]:stack+=[f] if stack[-1]+'/' not in f else []
        return stack
