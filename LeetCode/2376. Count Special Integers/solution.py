class Solution:
    def countSpecialNumbers(self, num: int) -> int:
        s = list(map(int,list(str(num))))
        n = len(s)
        ans = 0
        for i in range(1,n):
            ans += perm(10,i)-perm(9,i-1)
        for i in range(n):

            lo = 0
            if i == 0:
                lo = 1
            for ch in range(lo,s[i]):
                if ch in s[:i]:
                    continue 
                sz = i+1
                ans += perm(10-sz,n-sz)

            if s[i] in s[:i]:
                break
        return ans+(len(set(s))==len(s))