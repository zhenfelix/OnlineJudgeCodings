class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for i in range(k):
            cur = -heapq.heappop(piles)
            cur -= (cur//2)
            heapq.heappush(piles, -cur)
        return -sum(piles)