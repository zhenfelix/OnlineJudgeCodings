class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [d/s for d, s in zip(dist,speed)]
        heapq.heapify(time)
        cur, cnt = 0, 0
        while time:
            # print(time)
            if cur >= time[0]:
                break
            heapq.heappop(time)
            cnt += 1
            cur += 1
        return cnt 