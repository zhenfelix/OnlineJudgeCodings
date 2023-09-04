class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        s = s1 = sum(nums1)
        if s <= x:
            return 0
        s2 = sum(nums2)
        arr = [(b,a) for a, b in zip(nums1,nums2)]
        arr.sort()
        dp = [0]*n 
        for k in range(n):
            s += s2 
            ndp = dp[:]
            for i in range(k,n):
                ndp[i] = max(ndp[i-1], dp[i-1]+(k+1)*arr[i][0]+arr[i][1])
            if s-ndp[-1] <= x:
                return k+1
            dp = ndp
        return -1

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        v1 = sum(nums1)
        v2 = sum(nums2)
        
        n = len(nums1)
        sorted_range = sorted(range(n), key=lambda x: nums2[x])
        dp = [-inf] * (n + 1)
        dp[0] = 0
        for i in sorted_range:
            for j in range(n, 0, -1):
                dp[j] = max(dp[j], dp[j-1] + nums1[i] + nums2[i] * j)
        
        for i in range(n + 1):
            if v1 + v2 * i - dp[i] <= x:
                return i
        return -1


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/N76IWK/view/qMiuH1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。