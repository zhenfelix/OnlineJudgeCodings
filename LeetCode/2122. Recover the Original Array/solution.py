class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)//2
        def dfs(j):
            q = [v for v in nums]
            cc = Counter(nums)
            delta = nums[j]-nums[0]
            if delta%2 == 1 or delta == 0:
                return []
            res = []
            while q:
                cur = heapq.heappop(q)
                if cc[cur] <= 0:
                    continue
                cc[cur] -= 1
                if cc[cur+delta] <= 0:
                    break
                cc[cur+delta] -= 1
                res.append(cur+delta//2)
            return res
        for i in range(1,n+1):
            ans = dfs(i)
            if len(ans) == n:
                return ans
        return []



class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)//2
        def dfs(j):
            cc = Counter(nums)
            delta = nums[j]-nums[0]
            if delta%2 == 1 or delta == 0:
                return []
            res = []
            for i, cur in enumerate(nums):
                if cc[cur] <= 0:
                    continue
                cc[cur] -= 1
                if cc[cur+delta] <= 0:
                    break
                cc[cur+delta] -= 1
                res.append(cur+delta//2)
            return res
        for i in range(1,n+1):
            ans = dfs(i)
            if len(ans) == n:
                return ans
        return []



class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        keys = sorted(list(set(nums)))
        for i in range(n - 2, n // 2 - 2, -1):
            delta = nums[n - 1] - nums[i]
            if delta == 0 or delta % 2 == 1:
                continue
            cnt = collections.Counter(nums)
            ok = True
            ans = []
            for key in keys:
                if cnt[key] == 0:
                    continue
                if cnt[key + delta] < cnt[key]:
                    ok = False
                    break
                cnt[key + delta] -= cnt[key]
                ans += [key + delta // 2] * cnt[key]
                cnt[key] = 0
            if ok:
                return ans
        return []


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/NS4Y2j/view/dIMeD8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。