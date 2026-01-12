class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        d = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
        m, tr = len(d), [0] * (len(d) + 1)

        def u(i, v):
            while i <= m: tr[i] += v; i += i & -i

        def q(i):
            s = 0
            while i: s += tr[i]; i -= i & -i
            return s

        cur = 0
        for i, x in enumerate(nums[:k]):
            r = d[x]
            cur += i - q(r)
            u(r, 1)
        
        ans = cur
        for i in range(k, len(nums)):
            r_out = d[nums[i-k]]
            u(r_out, -1)
            cur -= q(r_out - 1)

            r_in = d[nums[i]]
            cur += k - 1 - q(r_in)
            u(r_in, 1)

            if cur < ans: ans = cur
            
        return ans