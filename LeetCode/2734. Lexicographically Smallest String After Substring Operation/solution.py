class Solution:
    def smallestString(self, s: str) -> str:    
        cnt, cur = 1, 0
        n = len(s)
        arr = list(s)
        for i in range(n):
            if s[i] != 'a' and cnt > 0:
                cnt -= 1
                cur = 1
            if s[i] == 'a':
                cur = 0
            if cur == 1:
                arr[i] = chr(ord(arr[i])-1)
        return ''.join(arr) if cnt == 0 else s[:-1]+'z'
