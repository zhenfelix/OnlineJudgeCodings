class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        state = ''.join(map(str,[board[0]]+[board[1]]))
        visited = set([state])
        q = deque([state])
        step = 0
        def swap(i,j,s):
            i, j = min(i,j), max(i,j)
            return s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
        while q:
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                if cur == '123450':
                    return step
                idx = cur.index('0')
                for new_idx in [-3,3]:
                    new_idx += idx 
                    if 0 <= new_idx < 2:
                        nxt = swap(idx,new_idx,cur)
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
                for new_idx in [-1,1]:
                    new_idx += idx
                    if new_idx//3 == idx//3:
                        nxt = swap(idx,new_idx,cur)
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
            step += 1
        return -1

