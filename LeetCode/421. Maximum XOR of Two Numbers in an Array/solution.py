class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(bin(max(nums))) - 2
        root = dict()
        def add(x):
            cur = root
            for i in range(max_len)[::-1]:
                bit = (x>>i)&1
                if bit not in cur:
                    cur[bit] = dict()
                cur = cur[bit]
        ans = 0
        for x in nums:
            add(x)
            cur = root
            tmp = 0
            for i in range(max_len)[::-1]:
                bit = (x>>i)&1
                bit = 1^bit
                if bit in cur:
                    cur = cur[bit]
                    tmp |= (1<<i)
                else:
                    cur = cur[bit^1]
            ans = max(ans, tmp)
        return ans



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        max_len = len(bin(max(nums))) - 2
        for i in range(max_len - 1, -1, -1):
            cur = 1 << i
            res |= cur
            d = {}
            find = 0
            for num in nums:
                d[num & res] = 1
                if (num & res) ^ res in d:
                    find = 1
                    break
            if not find:
                res ^= 1 << i
        return res
