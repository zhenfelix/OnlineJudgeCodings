class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = collections.deque()
        visited = set()
        q.append(start)
        visited.add(start)
        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            for nxt in [cur-arr[cur], cur+arr[cur]]:
                if 0 <= nxt < n and nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)
        return False