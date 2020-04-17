# import heapq
# class Solution:
#     def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
#         q = [(-v,k) for k,v in Counter(barcodes).items()]
#         heapq.heapify(q)
#         res = [0]
#         while q:
#             cnt, ch = heapq.heappop(q)
#             cnt += 1
#             if ch == res[-1]:
#                 cnt_, ch_ = heapq.heappop(q)
#                 cnt_ += 1
#                 res.append(ch_)
#                 if cnt_ < 0:
#                     heapq.heappush(q,(cnt_,ch_))
#             res.append(ch)
#             if cnt < 0:
#                 heapq.heappush(q,(cnt,ch))
#         return res[1:]
        
    
    
class Solution:
    def rearrangeBarcodes(self, packages):
        i, n = 0, len(packages)
        res = [0] * n
        for k, v in collections.Counter(packages).most_common():
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n: i = 1
        return res
            