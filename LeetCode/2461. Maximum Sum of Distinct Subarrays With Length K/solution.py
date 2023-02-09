class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        seen = defaultdict(lambda: -1)
        n = len(nums)
        presums = [0]
        for a in nums:
            presums.append(presums[-1]+a)
        left = -1
        for right in range(n):
            a = nums[right]
            left = max(left,seen[a])
            left = max(left,right-k)
            if right-left == k:
                ans = max(ans, presums[right+1]-presums[left+1])
                # print(left,right)
            seen[a] = right
        return ans 


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter(nums[:k - 1])
        s = sum(nums[:k - 1])
        for in_, out in zip(nums[k - 1:], nums):
            cnt[in_] += 1  # 移入元素
            s += in_
            if len(cnt) == k:
                ans = max(ans, s)
            cnt[out] -= 1  # 移出元素
            if cnt[out] == 0:
                del cnt[out]  # 重要：及时移除个数为 0 的数据
            s -= out
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/HhkSf4/view/pK06Qb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。