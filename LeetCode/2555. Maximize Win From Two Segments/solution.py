class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        def check(arr):
            cnt = [0]*n
            left = 0
            for right in range(n):
                while arr[right]-arr[left] > k:
                     left += 1  
                cnt[right] = right-left+1 
                if right: cnt[right] = max(cnt[right], cnt[right-1])
            return cnt 
        l, r = check(prizePositions), check([-x for x in prizePositions[::-1]])[::-1]
        # print(l,r)
        return max([l[i]+r[i+1] for i in range(n-1)],default=1)

