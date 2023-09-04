class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        mp = defaultdict(list)
        for i, v in enumerate(nums):
            mp[v].append(i)
        ans = 0
        for _, arr in mp.items():
            n = len(arr)
            l, s, cur = 0, 0, 1
            ans = max(ans, cur)
            for r in range(1,n):
                cur += 1
                s += arr[r]-arr[r-1]-1
                while s > k:
                    cur -= 1
                    l += 1
                    s -= (arr[l]-arr[l-1]-1)
                ans = max(ans, cur)
        return ans 


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = [[] for _ in range(len(nums) + 1)]
        for i, x in enumerate(nums):
            pos[x].append(i - len(pos[x]))
        ans = 0
        for ps in pos:
            left = 0
            for right, p in enumerate(ps):
                while p - ps[left] > k:  # 要删除的数太多了
                    left += 1
                ans = max(ans, right - left + 1)
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/SIJedb/view/ZVZvhi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。