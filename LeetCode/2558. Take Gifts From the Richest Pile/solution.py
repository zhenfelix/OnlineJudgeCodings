class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        hq = [-x for x in gifts]
        heapify(hq)
        for _ in range(k):
            x = -heappop(hq)
            # print(x,int(math.sqrt(x)))
            heappush(hq, -int(math.sqrt(x)))
        return -sum(hq)