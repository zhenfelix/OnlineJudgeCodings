class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if n < 2 or stones[0] != 0 or stones[1] != 1:
            return False
        q = collections.deque()
        visited = set()
        q.append((1,1))
        visited.add((1,1))
        while q:
            idx, k = q.popleft()
            if idx == n-1:
                return True
            for i in range(idx+1,n):
                step = stones[i] - stones[idx]
                if step > k + 1:
                    break
                if step >= k - 1 and (i,step) not in visited:
                    q.append((i,step))
                    visited.add((i,step))
        return False
