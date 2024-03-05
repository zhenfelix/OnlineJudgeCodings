class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans = cnt = 0
        n = len(word)
        for i in range(1,n):
            if abs(ord(word[i])-ord(word[i-1])) <= 1:
                cnt += 1
            else:
                ans += (cnt+1)//2
                cnt = 0
        ans += (cnt+1)//2
        return ans 