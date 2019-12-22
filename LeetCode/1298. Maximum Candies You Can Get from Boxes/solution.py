class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        active = [0]*n
        q = collections.deque()
        visited = set()
        for box in initialBoxes:
            active[box] = 1
            if status[box] == 1:
                q.append(box)
                visited.add(box)
        res = 0
        while q:
            box = q.popleft()
            res += candies[box]
            for k in keys[box]:
                status[k] = 1
                if active[k] == 1 and k not in visited:
                    q.append(k)
                    visited.add(k)
            for nxt in containedBoxes[box]:
                active[nxt] = 1
                if status[nxt] == 1 and nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)
        return res