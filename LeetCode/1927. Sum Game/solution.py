class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        cnt, sums = 0, 0
        for i in range(n):
            delta = 1 if i < n//2 else -1
            if num[i] == '?':
                cnt += delta
            else:
                sums += delta*int(num[i])
        if abs(cnt)%2 == 1 or sums*cnt > 0:
            return True
        if abs(sums) == abs(cnt)//2*9:
            return False
        return True


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

        
