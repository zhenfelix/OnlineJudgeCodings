class SeatManager:

    def __init__(self, n: int):
        self.available = [i+1 for i in range(n)]
        heapq.heapify(self.available)


    def reserve(self) -> int:
        cur = heapq.heappop(self.available)
        return cur


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)




# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)