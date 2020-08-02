class Solution(object):
    def minFlips(self, target):
        flips = 0
        status = '0'
        for c in target:
            if c != status:
                flips += 1
                status = '0' if status == '1' else '1'
        return flips
        

    def minFlips(self, target: str) -> int:
        target = list(map(int,target))
        n = len(target)
        cnt = 0
        for i in range(n):
            if cnt%2 == target[i]:
                continue
            cnt += 1
        return cnt 
