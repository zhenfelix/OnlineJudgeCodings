# import functools


# class Solution:
#     def maxStudents(self, seats: List[List[str]]) -> int:
#         n, m = len(seats), len(seats[0])
#         mask = [0] * (n + 1)
#         for r in range(n):
#             for c in range(m):
#                 if seats[r][c] == '.':
#                     mask[r] |= (1 << c)

#         states_ = [[0] for _ in range(n+1)]
#         for r in range(n):
#             for ss in range(1<<m):
#                 if (ss&mask[r]) == ss:
#                     states_[r] += [ss]

#         # print(n, m, mask, states_)
        
#         @functools.lru_cache(None)
#         def check(state):
#             pre = 0
#             while state:
#                 cur = state & 1
#                 state >>= 1
#                 if pre and cur:
#                     return False
#                 pre = cur
#             return True

#         @functools.lru_cache(None)
#         def count(state):
#             sums = 0
#             while state:
#                 sums += (state & 1)
#                 state >>= 1
#             return sums

#         @functools.lru_cache(None)
#         def dfs(row, state):
#             if row < 0 or not check(state):
#                 return 0
#             sums = count(state)
#             # nxts = set([tmp & mask[row - 1] for tmp in range(1 << m)])
#             # print(row,state,sums,nxts)
#             sums += max(dfs(row - 1, nxt) for nxt in states_[row-1] if check(state | nxt))
#             return sums

#         return dfs(n, 0)

import functools
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        n, m = len(seats), len(seats[0])
        def Hungarian():
            total, res = 0, 0
            match = [[-1]*m for _ in range(n)]
            for r in range(n):
                for c in range(m):
                    if seats[r][c] == '.':
                        total += 1
                    # if c&1:
                    #     continue
                    if seats[r][c] == '.' and match[r][c] == -1:
                        visited = set()
                        if dfs(r,c,visited,match):
                            res += 1
            return total-res

        def dfs(r_,c_,visited_,match_):
            for dr in [-1,0,1]:
                for dc in [-1,1]:
                    x, y = r_+dr, c_+dc
                    if 0 <= x < n and 0 <= y < m and seats[x][y] == '.' and (x,y) not in visited_:
                        visited_.add((x,y))
                        if match_[x][y] == -1 or dfs(match_[x][y][0],match_[x][y][1],visited_,match_):
                            match_[x][y] = (r_,c_)
                            match_[r_][c_] = (x,y)
                            return True
            return False

        return Hungarian()



