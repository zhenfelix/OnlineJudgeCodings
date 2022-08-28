class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        fa = list(range(n + 1))
        sum = [0] * (n + 1)
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        ans = [0] * n
        for i in range(n - 1, 0, -1):
            x = removeQueries[i]
            to = find(x + 1)
            fa[x] = to  # 合并 x 和 x+1
            sum[to] += sum[x] + nums[x]
            ans[i - 1] = max(ans[i], sum[to])
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/maximum-segment-sum-after-removals/solution/by-endlesscheng-p61j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = [i for i in range(n)]
        tot = [0]*n 
        ans = [0]*n 
        res = 0
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def connect(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv 
                tot[rv] += tot[ru]
            return
        for i in range(n)[::-1]:
            q = removeQueries[i]
            tot[q] = nums[q]
            if q > 0 and tot[q-1] > 0:
                connect(q,q-1)
            if q+1 < n and tot[q+1] > 0:
                connect(q,q+1)
            if i > 0:
                res = max(res,tot[find(q)])
                ans[i-1] = res
        return ans 



from sortedcontainers import *
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        presums = [0]
        for x in nums:
            presums.append(presums[-1]+x)
        mp = [n]*n 
        intervals = SortedList([0])
        sums = SortedList([presums[-1]])
        ans = []
        for i in removeQueries:
            j = intervals.bisect_right(i)-1
            left = intervals[j]
            right = mp[left]
            intervals.remove(left)
            sums.remove(presums[right]-presums[left])
            if left < i:
                intervals.add(left)
                mp[left] = i 
                sums.add(presums[i]-presums[left])
            if i+1 < right:
                intervals.add(i+1)
                mp[i+1] = right
                sums.add(presums[right]-presums[i+1])
            if sums:
                ans.append(sums[-1])
            else:
                ans.append(0)
        return ans