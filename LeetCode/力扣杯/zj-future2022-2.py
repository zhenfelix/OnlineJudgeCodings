class Solution:
    def minSwaps(self, chess: List[int]) -> int:
        n = len(chess)
        presums = [0]
        ans = float('inf')
        tot = chess.count(1)
        for i in range(n):
            presums.append(presums[-1]+chess[i])
            if i+1 >= tot:
                ans = min(ans, tot-(presums[i+1]-presums[i+1-tot]))
        return ans