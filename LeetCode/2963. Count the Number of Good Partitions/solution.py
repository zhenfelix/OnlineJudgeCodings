class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        g = defaultdict(list)
        for i, v in enumerate(nums):
            g[v].append(i)
        intervals = []
        for v, arr in g.items():
            intervals.append((arr[0],arr[-1]))
        intervals.sort()
        cnt = 0
        reach = -1
        for l, r in intervals:
            if l > reach:
                cnt += 1
            reach = max(reach,r)
        return pow(2,cnt-1,MOD)