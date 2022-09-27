class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cnt = [0]*n 
        rooms = [(0,i) for i in range(n)]
        available = []
        # print(sorted(meetings))
        for s, e in sorted(meetings):
            # print(rooms)
            while rooms and rooms[0][0] <= s:
                heappush(available, heappop(rooms)[-1])
            if not available:
                a, i = heappop(rooms)
            else:
                a, i = s, heappop(available)
            # print(max(a, s),i)
            a = max(a, s) + e-s
            cnt[i] += 1
            heappush(rooms,(a,i))
        # print(cnt)
        return min(range(n), key=lambda x: (-cnt[x],x))