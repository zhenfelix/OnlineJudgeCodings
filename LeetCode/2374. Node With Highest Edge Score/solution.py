class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0]*n 
        for i, j in enumerate(edges):
            score[j] += i 
        ans = 0
        for i in range(n):
            if score[i] > score[ans]:
                ans = i
        return ans 