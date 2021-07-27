class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        cur = 0
        available = []
        seq = []
        seat = {}
        for i, se in enumerate(times):
            seq.append((se[0],1,i))
            seq.append((se[1],-1,i))
        seq.sort()
        for t, flag, i in seq:
            if flag == -1:
                heapq.heappush(available, seat[i])
            else:
                if available:
                    s = heapq.heappop(available)
                    seat[i] = s 
                else:
                    seat[i] = cur
                    cur += 1
        return seat[targetFriend]