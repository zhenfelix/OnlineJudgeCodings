import heapq

# class Solution:
#     def minBuildTime(self, blocks: List[int], split: int) -> int:
#         heapq.heapify(blocks)
#         while len(blocks) > 1:
#             # print(blocks)
#             x = heapq.heappop(blocks)
#             y = heapq.heappop(blocks)
#             xy = max(x, y) + split
#             heapq.heappush(blocks, xy)
#         return blocks[0]

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)
        while len(blocks) > 1:
            b1, b2 = heapq.heappop(blocks), heapq.heappop(blocks)
            heapq.heappush(blocks, b2+split)
        return heapq.heappop(blocks)