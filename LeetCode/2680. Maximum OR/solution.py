class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        pre, nxt = [0]*(n+1), [0]*(n+1)
        for i in range(n):
            pre[i] = pre[i-1]|nums[i]
        for i in range(n)[::-1]:
            nxt[i] = nxt[i+1]|nums[i]
        for i in range(n):
            ans = max(ans,pre[i-1]|nxt[i+1]|(nums[i]<<k))
        return ans 


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            suf[i] = suf[i + 1] | nums[i]
        ans = pre = 0
        for i, x in enumerate(nums):
            ans = max(ans, pre | (x << k) | suf[i + 1])
            pre |= x
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/OMJd2e/view/PrXhZ2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        nmax = 50
        ans = 0
        cnt = [0]*nmax
        for x in nums:
            for i in range(nmax):
                if x == 0: break
                if x&1:
                    cnt[i] += 1
                x >>= 1
        for x in nums:
            tmp = [0]*nmax
            for i in range(nmax):
                if x == 0: break
                if x&1:
                    tmp[i] += 1
                    cnt[i+k] += 1
                    cnt[i] -= 1
                x >>= 1
            y = 0
            for i in range(nmax):
                if cnt[i] > 0:
                    y |= (1<<i)
            for i in range(nmax):
                if tmp[i]:
                    cnt[i+k] -= 1
                    cnt[i] += 1
            ans = max(ans,y)
        return ans 