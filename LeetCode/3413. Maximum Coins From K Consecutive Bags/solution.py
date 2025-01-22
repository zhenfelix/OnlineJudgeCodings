class Solution:
    # 2271. 毯子覆盖的最多白色砖块数
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        ans = cover = left = 0
        for tl, tr, c in tiles:
            cover += (tr - tl + 1) * c
            while tiles[left][1] < tr - carpetLen + 1:
                cover -= (tiles[left][1] - tiles[left][0] + 1) * tiles[left][2]
                left += 1
            uncover = max((tr - carpetLen + 1 - tiles[left][0]) * tiles[left][2], 0)
            ans = max(ans, cover - uncover)
        return ans

    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort(key=lambda c: c[0])
        ans = self.maximumWhiteTiles(coins, k)

        coins.reverse()
        for t in coins:
            t[0], t[1] = -t[1], -t[0]
        return max(ans, self.maximumWhiteTiles(coins, k))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-coins-from-k-consecutive-bags/solutions/3039059/hua-dong-chuang-kou-hua-liang-bian-pytho-4u47/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maximumCoins(self, intervals: List[List[int]], dist: int) -> int:
        
        splits = []
        intervals.sort()
        arr = []
        pre = -inf
        for l, r, w in intervals:
            splits.append(l-1)
            splits.append(l-1+dist)
            splits.append(r)
            splits.append(r+dist)
            if l-pre > 0:
                arr.append([pre,l-1,0])
            arr.append([l,r,w])
            pre = r+1
        arr.append([pre,inf,0])

        def check(p):
            l, r = 0, len(arr)-1
            while l <= r:
                t = (l+r)//2
                if p >= arr[t][0]:
                    l = t+1
                else:
                    r = t-1
            return arr[r][-1]
                

        ans = cur = diff = 0
        splits.append(-1)
        splits = sorted(list(set(splits)))
        m = len(splits)
        # print(splits)

        for i in range(1,m):
            cur += diff*(splits[i]-splits[i-1])
            
            ans = max(ans,cur)
            p = splits[i]
            # print(diff,cur,p)
            diff = check(p+1)-check(p-dist+1)
        return ans 
        
