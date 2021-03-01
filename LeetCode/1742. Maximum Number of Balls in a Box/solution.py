class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cc = Counter()
        for i in range(lowLimit, highLimit+1):
            tmp = 0
            for ch in str(i):
                tmp += int(ch)
            # print(tmp)
            cc[tmp]+=1
        # print(cc)
        return max(cc.values())