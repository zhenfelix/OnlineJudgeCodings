# class Solution:
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
#         m,n=len(str1),len(str2)
#         dp={}
#         def lcs(i,j):
#             if (i,j) in dp:
#                 return dp[i,j]
#             if i<0 or j<0:
#                 dp[i,j]=""
#                 return dp[i,j]
#             if str1[i]==str2[j]:
#                 lcs(i-1,j-1)
#                 dp[i,j]=dp[i-1,j-1]+str1[i]
#                 return dp[i,j]
#             else:
#                 lcs(i,j-1)
#                 lcs(i-1,j)
#                 if len(dp[i,j-1])>len(dp[i-1,j]):
#                     dp[i,j]=dp[i,j-1]
#                 else:
#                     dp[i,j]=dp[i-1,j]
#                 return dp[i,j]
#         str_common=lcs(m-1,n-1)
#         l=len(str_common)
#         print(str_common)
#         ans=""
#         i,j,k=0,0,0
#         while i<m or j<n:
#             while i<m and (k>=l or str1[i]!=str_common[k]):
#                 ans+=str1[i]
#                 i+=1
#             while j<n and (k>=l or str2[j]!=str_common[k]):
#                 ans+=str2[j]
#                 j+=1
#             while i<m and j<n and str1[i]==str2[j]:
#                 ans+=str_common[k]
#                 i+=1
#                 j+=1
#                 k+=1
#         return ans

class Solution:
    def shortestCommonSupersequence(self, A, B):
        def lcs(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(m):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            return dp[-1][-1]

        res, i, j = "", 0, 0
        for c in lcs(A, B):
            while A[i] != c:
                res += A[i]
                i += 1
            while B[j] != c:
                res += B[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + A[i:] + B[j:]