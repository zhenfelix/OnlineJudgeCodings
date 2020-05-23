# class Solution:
#     def countTriplets(self, arr: List[int]) -> int:
#         mp = defaultdict(list)
#         mp[0].append(-1)
#         res, sums = 0, 0
#         for i, a in enumerate(arr):
#             sums ^= a 
#             for idx in mp[sums]:
#                 res += i-idx-1
#             mp[sums].append(i)
#         return res

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        mp = {}
        mp[0] = (0,1)
        res, sums = 0, 0
        for i, a in enumerate(arr):
            sums ^= a 
            if sums in mp:
                sumidx, cnt = mp[sums]
                res += i*cnt-sumidx
                sumidx += i+1
                cnt += 1
                mp[sums] = (sumidx,cnt)
            else:
                mp[sums] = (i+1,1)
        return res