class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(nums[0])
        candidates = [[i for i in range(n)]]
        for i in range(1,m+1):
            mp = [[] for _ in range(10)]
            for j in candidates[-1]:
                idx = ord(nums[j][-i])-ord('0')
                mp[idx].append(j)
            candidates.append([])
            for arr in mp:
                for a in arr:
                    candidates[-1].append(a)
        ans = []
        for k, t in queries:
            ans.append(candidates[t][k-1])
        return ans 


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(nums[0])
        candidates = []
        for i in range(m):
            tmp = list(range(n))
            tmp.sort(key = lambda x: nums[x][-(i+1):])
            candidates.append(tmp[:])
        # print(candidates)
        ans = []
        for k, t in queries:
            ans.append(candidates[t-1][k-1])
        return ans