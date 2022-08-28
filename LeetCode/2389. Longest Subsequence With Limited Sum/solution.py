class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        presums = [0]
        for x in nums:
            presums.append(presums[-1]+x)
        ans = []
        for q in queries:
            ans.append(bisect.bisect_right(presums,q)-1)
        return ans

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n, m = len(nums), len(queries)
        ans = [0]*m 
        for i, q in enumerate(queries):
            s, cnt = 0, 0
            for x in nums:
                if s+x > q:
                    break
                s += x
                cnt += 1
            ans[i] = cnt
        return ans