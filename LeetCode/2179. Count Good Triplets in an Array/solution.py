class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        N = n+5
        tree = [0]*N 
        def init():
            for i in range(N):
                tree[i] = 0
            return

        def query(x):
            val = 0
            while x:
                val += tree[x]
                x -= x&(-x)
            return val

        def update(x, delta):
            while x < N:
                tree[x] += delta
                x += x&(-x)
            return

        pos = [-1]*n 
        dp = [[1]*n for _ in range(3)]
        for i, v in enumerate(nums2):
            pos[v] = i 
        for i in range(1,3):
            init()
            for j in range(n):
                dp[i][j] = query(pos[nums1[j]])
                update(pos[nums1[j]]+1, dp[i-1][j])
        return sum(dp[-1])



class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        p = [0] * n
        for i, x in enumerate(nums1):
            p[x] = i
        ans = 0
        tree = [0] * (n + 1)
        for i in range(1, n - 1):
            # 将 p[nums2[i - 1]] + 1 加入树状数组
            j = p[nums2[i - 1]] + 1
            while j <= n:
                tree[j] += 1
                j += j & -j
            # 计算 less
            y, less = p[nums2[i]], 0
            j = y
            while j:
                less += tree[j]
                j &= j - 1
            ans += less * (n - 1 - y - (i - less))
        return ans


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/count-good-triplets-in-an-array/solution/deng-jie-zhuan-huan-shu-zhuang-shu-zu-by-xmyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        p = [0] * n
        for i, x in enumerate(nums1):
            p[x] = i
        ans = 0
        s = SortedList()
        for i in range(1, n - 1):
            s.add(p[nums2[i - 1]])
            y = p[nums2[i]]
            less = s.bisect_left(y)
            ans += less * (n - 1 - y - (i - less))
        return ans


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/count-good-triplets-in-an-array/solution/deng-jie-zhuan-huan-shu-zhuang-shu-zu-by-xmyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。