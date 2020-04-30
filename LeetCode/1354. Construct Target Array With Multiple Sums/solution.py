class Solution:
    # def isPossible(self, target: List[int]) -> bool:
    #     sums = sum(target)
    #     target = [-t for t in target]
    #     heapq.heapify(target)
    #     while target:
    #         # print(target)
    #         cur = -heapq.heappop(target)
    #         if cur > 1:
    #             remains = sums - cur
    #             if cur <= remains or remains <= 0:
    #                 return False
    #             cur = cur%remains or remains
    #             sums = remains + cur
    #             heapq.heappush(target,-cur)
    #     return True
    
    def isPossible(self, A):
        total = sum(A)
        A = [-a for a in A]
        heapq.heapify(A)
        while True:
            a = -heapq.heappop(A)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)