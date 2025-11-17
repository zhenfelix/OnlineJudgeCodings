class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # 见 560 题
        pre_sum = 0  # 前缀和
        last_start = 0  # 上一个连续相同段的起始下标
        ans = 0

        for i, x in enumerate(nums):
            if i and x != nums[i - 1]:
                # 上一个连续相同段结束，可以把上一段对应的前缀和添加到 cnt
                v = nums[i - 1]
                s = pre_sum
                for _ in range(i - last_start):
                    cnt[s % k] += 1
                    s -= v
                last_start = i

            pre_sum += x
            ans += cnt[pre_sum % k]

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/solutions/3815647/qian-zhui-he-yu-ha-xi-biao-bi-mian-zhong-nc4l/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        cc = Counter()
        s = d = ans = 0
        cc[0] = 1
        n = len(nums)
        pre = 0
        for i in range(n):
            if nums[i] != nums[pre]:
                d = 0
                for j in range(pre,i):
                    s += nums[j]
                    s %= k
                    cc[s] += 1
                pre = i 
            d += nums[i]
            d %= k 
            # if d == 0:
            #     ans += 1
            ans += cc[(s+d)%k]
        return ans 