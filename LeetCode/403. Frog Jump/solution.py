class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mx = max(stones)
        pos = set(stones)
        visited = set()
        visited.add((0,0))
        q = deque()
        q.append((0,0))
        while q:
            dis, speed = q.popleft()
            if dis == mx:
                return True
            for nxt in range(speed-1,speed+2):
                if dis+nxt in pos and (dis+nxt,nxt) not in visited:
                    visited.add((dis+nxt,nxt))
                    q.append((dis+nxt,nxt))
        return False


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
