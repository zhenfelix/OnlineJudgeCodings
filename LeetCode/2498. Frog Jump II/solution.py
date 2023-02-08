class Solution:

    def maxJump(self, stones: List[int]) -> int:

        ans = stones[1] - stones[0]

        for i in range(2, len(stones)):

            ans = max(ans, stones[i] - stones[i - 2])

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/frog-jump-ii/solutions/2015696/tan-xin-by-endlesscheng-wj2k/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def maxJump(self, stones: List[int]) -> int:
        lo, hi = 1, stones[-1]-stones[0]
        stones.append(0)
        def check(t):
            n = len(stones)
            pre = [-1]*n 
            j = 0
            pq = [0]
            for i in range(1,n-1):
                while pq and stones[i]-stones[pq[0]] > t:
                    heappop(pq)
                if not pq:
                    return False
                j = pq[0]
                if j < i-1:
                    pre[i] = i-1
                else:
                    pre[i] = pre[j]
                if stones[i+1]-stones[pre[i]] <= t:
                    heappush(pq,i)
            return stones[n-1]-stones[pre[n-1]] <= t 

        while lo <= hi:
            m = (lo+hi)//2
            if check(m):
                hi = m-1
            else:
                lo = m+1
        return lo