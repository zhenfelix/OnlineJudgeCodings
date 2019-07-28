from collections import deque

# class Solution:
#     def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
#         red_mp = {}
#         blue_mp = {}
#         ans = [-1]*n
#         # blue = [-1]*n
#         for e in red_edges:
#             if e[0] not in red_mp:
#                 red_mp[e[0]] = [e[1]]
#             else:
#                 red_mp[e[0]] += [e[1]]
#         for e in blue_edges:
#             if e[0] not in blue_mp:
#                 blue_mp[e[0]] = [e[1]]
#             else:
#                 blue_mp[e[0]] += [e[1]]
                
#         q = deque()
#         q.append(0)
#         level = 0
#         mp = [red_mp,blue_mp]
#         visited = [0]*n
#         visited[0] |= (1<<1)
#         while len(q) > 0:
#             nq = len(q)
#             idx = level%2
#             for _ in range(nq):
#                 front = q.popleft()
#                 if ans[front] == -1:
#                     ans[front] = level
#                 else:
#                     ans[front] = min(ans[front],level)
                
#                 if front not in mp[idx]:
#                     continue
#                 tmp = visited.copy()
#                 for out in mp[idx][front]:
                    
#                     if visited[out] & (1<<idx):
#                         continue
#                     else:
#                         tmp[out] |= (1<<idx)
#                         q.append(out)
#                 visited = tmp
                
#             level += 1
            
#         q = deque()
#         q.append(0)
#         level = 0
#         mp = [blue_mp,red_mp,]
#         visited = [0]*n
#         visited[0] |= (1<<1)
#         while len(q) > 0:
#             nq = len(q)
#             idx = level%2
#             for _ in range(nq):
#                 front = q.popleft()
#                 if ans[front] == -1:
#                     ans[front] = level
#                 else:
#                     ans[front] = min(ans[front],level)
                
#                 if front not in mp[idx]:
#                     continue
#                 tmp = visited.copy()
#                 for out in mp[idx][front]:
#                     if visited[out] & (1<<idx):
#                         continue
#                     else:
#                         tmp[out] |= (1<<idx)
#                         q.append(out)
#                 visited = tmp
                
#             level += 1
        
#         return ans


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        reds = collections.defaultdict(list)
        blues = collections.defaultdict(list)
        for i, j in red_edges:
            reds[i].append(j)
        for i, j in blue_edges:
            blues[i].append(j)
        # print(reds, blues)
        frontier = collections.deque([(v, 'r') for v in reds[0]] + [(v, 'b') for v in blues[0]])
        # print(frontier)
        ans = [-1] * n
        ans[0] = 0
        step = 0
        seen = {(0, 'r'), (0, 'b')}
        for node, c in frontier:
            seen.add((node, c))
        while frontier:
            step += 1
            sz = len(frontier)
            for _ in range(sz):
                node, color = frontier.popleft()
                if ans[node] == -1:
                    ans[node] = step
                nei_lst = blues if color == 'r' else reds
                for nei in nei_lst[node]:
                    new_color = 'r' if color == 'b' else 'b'
                    if (nei, new_color) not in seen:
                        seen.add((nei, new_color))
                        frontier.append((nei, new_color))
        return ans