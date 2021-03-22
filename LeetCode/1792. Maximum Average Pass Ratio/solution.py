class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = [(x/y-(x+1)/(y+1),x,y) for x, y in classes]
        heapq.heapify(q)
        for _ in range(extraStudents):
            _, x, y = heapq.heappop(q)
            x += 1
            y += 1
            heapq.heappush(q, (x/y-(x+1)/(y+1),x,y))
        return sum(x/y for _, x, y in q)/len(q)