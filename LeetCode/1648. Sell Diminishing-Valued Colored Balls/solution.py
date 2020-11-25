class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        res, cnt, MOD = 0, 1, 10**9+7
        for hi, lo in zip(inventory,inventory[1:]):
            # print(hi,lo)
            if orders < (hi-lo)*cnt:
                cur = hi - orders//cnt
                res += (hi+cur+1)*(hi-cur)*cnt//2
                res += cur*(orders%cnt)
                res %= MOD
                orders = 0
                break
            if hi > lo:
                res += (hi+lo+1)*(hi-lo)*cnt//2
                res %= MOD
                orders -= (hi-lo)*cnt
            cnt += 1
        return res 


# import bisect
# class Solution:
#     def maxProfit(self, inventory: List[int], orders: int) -> int:
#         res = 0
#         MOD = 10**9+7
#         inventory.sort()
#         lo, hi = 0, 10**9
#         while lo <= hi:
#             mid = (lo+hi)//2
#             idx = bisect.bisect_left(inventory,mid)
#             cnt = sum(inventory[i]-mid for i in range(idx,len(inventory)))
#             if cnt < orders:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         for i, cur in enumerate(inventory):
#             if cur > lo:
#                 orders -= cur-lo
#                 res += (cur+lo+1)*(cur-lo)//2
#                 res %= MOD
#         res += orders*lo
#         res %= MOD
#         return res