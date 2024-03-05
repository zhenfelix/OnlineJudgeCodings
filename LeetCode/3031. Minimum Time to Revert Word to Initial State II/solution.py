class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        l = r = 0
        z = [0]*n 
        for i in range(1,n):
            if i < r:
                z[i] = min(r-i,z[i-l])
            while i+z[i] < n and word[z[i]] == word[i+z[i]]:
                z[i] += 1
            if i+z[i] > r:
                l, r = i, i+z[i]
            if i+z[i] == n and (n-z[i])%k == 0:
                return (n-z[i])//k
        return (n-1)//k+1

class Solution:
    def minimumTimeToInitialState(self, s: str, k: int) -> int:
        n = len(s)
        fail = [-1]*n  
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1
        j = n-1
        # print(fail)
        while j != -1:
            # print(j)
            j = fail[j]
            if (n-(j+1))%k == 0: return (n-(j+1))//k
            
        return (n-1)//k+1

