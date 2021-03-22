# class Solution:
#     def slidingPuzzle(self, board: List[List[int]]) -> int:
#         state = ''.join(map(str,[board[0]]+[board[1]]))
#         visited = set([state])
#         q = deque([state])
#         step = 0
#         def swap(i,j,s):
#             i, j = min(i,j), max(i,j)
#             return s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
#         while q:
#             n = len(q)
#             for _ in range(n):
#                 cur = q.popleft()
#                 if cur == '123450':
#                     return step
#                 idx = cur.index('0')
#                 for new_idx in [-3,3]:
#                     new_idx += idx 
#                     if 0 <= new_idx < 2:
#                         nxt = swap(idx,new_idx,cur)
#                         if nxt not in visited:
#                             visited.add(nxt)
#                             q.append(nxt)
#                 for new_idx in [-1,1]:
#                     new_idx += idx
#                     if new_idx//3 == idx//3:
#                         nxt = swap(idx,new_idx,cur)
#                         if nxt not in visited:
#                             visited.add(nxt)
#                             q.append(nxt)
#             step += 1
#         return -1



class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def generate(state):
            idx = state.find('0')
            r, c = idx//3, idx%3
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dr += r
                dc += c 
                if 0 <= dr < 2 and 0 <= dc < 3:
                    jdx = dr*3 + dc
                    i, j = min(idx,jdx), max(idx,jdx)
                    yield state[:i]+state[j]+state[i+1:j]+state[i]+state[j+1:]
            return

        cur = ''.join([str(x) for rows in board for x in rows])
        q = deque()
        seen = set()
        q.append(cur)
        seen.add(cur)
        step = 0
        while q:
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                if cur == "123450":
                    return step
                for nxt in generate(cur):
                    if nxt not in seen:
                        q.append(nxt)
                        seen.add(nxt)
            step += 1
        return -1
