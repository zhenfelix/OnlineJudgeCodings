# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1, v2 = version1.split("."), version2.split(".")
#         v1 = [int(v) for v in v1]
#         v2 = [int(v) for v in v2]
#         n1, n2 = len(v1), len(v2)
#         flag = 1
#         # print(v1,v2)
#         if n1 > n2:
#             n1, n2 = n2, n1
#             v1, v2 = v2, v1 
#             flag = -1
#         for i in range(n1):
#             if v1[i] > v2[i]:
#                 return 1*flag
#             elif v1[i] < v2[i]:
#                 return -1*flag
#         # print(v1,v2,i,n1,n2)
#         for j in range(i+1,n2):
#             # print("ok",j)
#             if v2[j] != 0:
#                 return -1*flag
#         return 0
            
            
# class Solution:        
#     def compareVersion(self, v1, v2):
#         v1, v2 = map(int, v1.split('.')), map(int, v2.split('.'))
#         v1, v2 = zip(*itertools.zip_longest(v1, v2, fillvalue = 0))
#         return (0, 1, -1)[(v1 > v2) - (v1 < v2)]
    
class Solution:
    def compareVersion(self, version1, version2):
            versions1 = [int(v) for v in version1.split(".")]
            versions2 = [int(v) for v in version2.split(".")]
            for i in range(max(len(versions1),len(versions2))):
                v1 = versions1[i] if i < len(versions1) else 0
                v2 = versions2[i] if i < len(versions2) else 0
                if v1 > v2:
                    return 1
                elif v1 < v2:
                    return -1
            return 0