class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        tot = sum(reward2)
        hq = [r2-r1 for r1,r2 in zip(reward1,reward2)]
        heapify(hq)
        for _ in range(k):
            tot -= heappop(hq)
        return tot 