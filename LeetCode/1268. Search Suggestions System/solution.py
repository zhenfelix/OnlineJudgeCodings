# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         search = ""
#         pos, n = 0, len(products)
#         ans = list()
#         for ch in searchWord:
#             search += ch
#             while pos < n and products[pos] < search:
#                 pos += 1
#             result = list()
#             for i in range(3):
#                 if pos + i < n and products[pos + i].startswith(search):
#                     result.append(products[pos + i])
#                 else:
#                     break
#             ans.append(result)
#         return ans

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         idx, n = 0, len(products)
#         print(len(products),len(searchWord))
#         print(products)
#         res = []
#         for j in range(len(searchWord)):
#             res.append([])
#             while idx < n and (j >= len(products[idx]) or products[idx][j] < searchWord[j]):
#                 idx += 1
#             for i in range(idx,idx+3):
#                 if i < n and j < len(products[i]) and products[i][j] == searchWord[j]:
#                     res[-1].append(products[i])
#                 else:
#                     break
#         return res
# not considering the prefix wrong answer


# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         idx, n = 0, len(products)
#         res = []
#         for j in range(len(searchWord)):
#             res.append([])
#             i = 0
#             for _ in range(3):
#                 while i < n and (products[i][:j+1] != searchWord[:j+1]):
#                     i += 1
#                 if i < n and products[i][:j+1] == searchWord[:j+1]:
#                     res[-1].append(products[i])
#                 i += 1
#         return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def lowerBound(i,j,k):
            while i <= j:
                mid = (i+j)//2
                if k >= len(products[mid]) or products[mid][k] <  searchWord[k]:
                    i = mid+1
                else:
                    j = mid-1
            return i 
        def upperBound(i,j,k):
            while i <= j:
                mid = (i+j)//2
                if k >= len(products[mid]) or products[mid][k] <= searchWord[k]:
                    i = mid+1
                else:
                    j = mid-1
            return j
            
        products.sort()
        left, right = 0, len(products)-1
        ans = list()
        for idx in range(len(searchWord)):
            left, right = lowerBound(left,right,idx), upperBound(left,right,idx)
            result = list()
            for pos in range(left,min(left+3,right+1)):
                result.append(products[pos])
            ans.append(result)
        return ans