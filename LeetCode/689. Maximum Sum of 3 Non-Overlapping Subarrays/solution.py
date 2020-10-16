from functools  import lru_cache
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], K: int) -> List[int]:
        prefix = [0] + nums
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]

        @lru_cache(None)
        def dfs(idx, t):
            cur, pos = 0, []
            if t > 0:
                cur, pos = dfs(idx-K, t-1)
                cur += prefix[idx+1] - prefix[idx-K+1]
                pos += [idx+1-K]
                if idx + 1 > t*K:
                    cur_, pos_ = dfs(idx-1, t)
                    if cur_ > cur or (cur_ == cur and tuple(pos_) < tuple(pos)):
                        cur, pos =  cur_, pos_
            # print(idx,t,cur,pos)
            return cur, pos.copy()
        return dfs(len(nums)-1, 3)[-1]