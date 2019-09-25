class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(arr):
            Next = [-1]*(n+1)
            i, j = 0, -1
            while i < n:
                if j == -1 or arr[i] == arr[j]:
                    j += 1
                    i += 1
                    Next[i] = j
                else:
                    j = Next[j]
            return Next
        
        n = len(s)
        dp = kmp(s)
        # print(dp)
        return dp[-1] > 0 and n%(n-dp[-1]) == 0
        