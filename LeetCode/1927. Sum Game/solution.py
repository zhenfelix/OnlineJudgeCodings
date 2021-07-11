class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        n //= 2
        diff, cnt = 0, 0
        for i in range(n*2):
            if num[i] == '?':
                if i < n:
                    cnt -= 1
                else:
                    cnt += 1
            else:
                val = ord(num[i])-ord('0')
                if i < n:
                    diff += val 
                else:
                    diff -= val 
        if cnt&1 or cnt*diff < 0:
            return True
        k = cnt//2 
        return diff != k*9

        
