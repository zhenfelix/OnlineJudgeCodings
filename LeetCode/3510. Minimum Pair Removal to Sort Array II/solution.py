class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList()  # (相邻元素和，左边那个数的下标)
        idx = SortedList(range(n))  # 剩余下标
        dec = 0  # 递减的相邻对的个数

        for i, (x, y) in enumerate(pairwise(nums)):
            if x > y:
                dec += 1
            sl.add((x + y, i))

        ans = 0
        while dec:
            ans += 1

            s, i = sl.pop(0)  # 删除相邻元素和最小的一对
            k = idx.bisect_left(i)

            # (当前元素，下一个数)
            nxt = idx[k + 1]
            if nums[i] > nums[nxt]:  # 旧数据
                dec -= 1

            # (前一个数，当前元素)
            if k:
                pre = idx[k - 1]
                if nums[pre] > nums[i]:  # 旧数据
                    dec -= 1
                if nums[pre] > s:  # 新数据
                    dec += 1
                sl.remove((nums[pre] + nums[i], pre))
                sl.add((nums[pre] + s, pre))

            # (下一个数，下下一个数)
            if k + 2 < len(idx):
                nxt2 = idx[k + 2]
                if nums[nxt] > nums[nxt2]:  # 旧数据
                    dec -= 1
                if s > nums[nxt2]:  # 新数据（当前元素，下下一个数）
                    dec += 1
                sl.remove((nums[nxt] + nums[nxt2], nxt))
                sl.add((s + nums[nxt2], i))

            nums[i] = s
            idx.remove(nxt)

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/solutions/3641787/mo-ni-liang-ge-you-xu-ji-he-by-endlessch-gx8s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。