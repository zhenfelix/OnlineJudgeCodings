class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        suffix = Counter(nums)
        prefix = Counter()
        ans = comb(n,5)
        for left, x in enumerate(nums[:-2]):
            suffix[x] -= 1
            if left > 1:
                right = n-1-left
                pre_x = prefix[x]
                suf_x = suffix[x]
                ans -= comb(left-pre_x,2)*comb(right-suf_x,2)
                for y, suf_y in suffix.items():
                    if y == x: continue
                    # print(right,suf_x,suf_y)
                    pre_y = prefix[y]
                    ans -= comb(pre_x,1)*comb(left-pre_x,1)*comb(suf_y,2)
                    ans -= comb(pre_x,1)*comb(pre_y,1)*comb(suf_y,1)*comb(right-suf_x-suf_y,1)
                    ans -= comb(pre_y,2)*comb(suf_x,1)*comb(right-suf_x,1)
                    ans -= comb(pre_y,1)*comb(left-pre_x-pre_y,1)*comb(suf_x,1)*comb(suf_y,1)
            prefix[x] += 1
        return ans%MOD 