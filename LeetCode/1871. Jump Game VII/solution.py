class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == '1':
            return False
        q = deque()
        q.append(0)
        reach = 0
        while q:
            cur = q.popleft()
            if cur == n-1:
                return True
            mi = max(reach+1,cur+minJump)
            mx = min(n,cur+maxJump+1)
            for nxt in range(mi, mx):
                if s[nxt] == '0':
                    q.append(nxt)
                reach = max(reach, nxt)
        return False

