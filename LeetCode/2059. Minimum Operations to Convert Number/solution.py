class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visited = set()
        q = deque()
        visited.add(start)
        q.append(start)
        step = 0
        while q:
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                for x in nums:
                    for y in [cur+x,cur-x,cur^x]:
                        if y == goal:
                            return step+1
                        if 0 <= y <= 1000 and y not in visited:
                            visited.add(y)
                            q.append(y)
            step += 1 
        return -1