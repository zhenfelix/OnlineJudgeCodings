class Solution:
    def fillCups(self, amount: List[int]) -> int:
        mx, s = max(amount), sum(amount)
        return max(mx, (s+1)//2)


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        amount = [-a for a in amount if a > 0]
        heapq.heapify(amount)
        while amount:
            a = -heapq.heappop(amount)
            if amount:
                b = -heapq.heappop(amount)
                if b > 1:
                    heapq.heappush(amount, -(b-1))
            if a > 1:
                heapq.heappush(amount, -(a-1))
            ans += 1
        return ans