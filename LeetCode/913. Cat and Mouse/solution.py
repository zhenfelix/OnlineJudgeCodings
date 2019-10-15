# class Solution:
#     def catMouseGame(self, graph: List[List[int]]) -> int:
#         def dfs(mouse, cat, mouseMove, visited):
#             # print(mouse, cat, mouseMove, visited)
#             if cat == mouse:
#                 return 2
#             if mouse == 0:
#                 return 1
#             if (mouse, cat, mouseMove) in visited:
#                 return 0
#             visited.append((mouse, cat, mouseMove))
#             if mouseMove:
#                 win, even = False, False
#                 for nxt in graph[mouse]:

#                     res = dfs(nxt, cat, False, visited)

#                     if res == 1:
#                         win = True
#                         break
#                     if res == 0:
#                         even = True
#             else:
#                 win, even = False, False
#                 for nxt in graph[cat]:
#                     if nxt == 0:
#                         continue

#                     res = dfs(mouse, nxt, True, visited)

#                     if res == 2:
#                         win = True
#                         break
#                     if res == 0:
#                         even = True

#             visited.pop()
#             # print(mouse, cat, mouseMove, visited)
#             # print(win,even)
#             if win:
#                 if mouseMove:
#                     return  1
#                 else:
#                     return  2
#             if even:
#                 return 0
#             if mouseMove:
#                 return  2
#             else:
#                 return  1

#         return dfs(1, 2, True, [])



# from collections import deque, defaultdict

# class Solution:
#     def catMouseGame(self, graph: List[List[int]]) -> int:
#         n = len(graph)
#         q = []
#         state = defaultdict(int)
#         for cat in range(1,n):
#             state[0,cat,True] = 1
#             state[0,cat,False] = 1 
            
#         for pos in range(1,n):
#             state[pos,pos,True] = 2
#             state[pos,pos,False] = 2
        
#         q = list(state.keys())
#         while q:
#             mouse, cat, mouseMove = q.pop()
#             score = state[mouse,cat,mouseMove]
#             if mouseMove:
#                 if score == 2:
#                     for parent in graph[cat]:
#                         if parent != 0 and state[mouse,parent,False] == 0:
#                             state[mouse,parent,False] = 2
#                             q.append((mouse,parent,False))
#                 else:
#                     for parent in graph[cat]:
#                         if parent != 0 and state[mouse,parent,False] == 0:
#                             all_lose = True
#                             for child in graph[parent]:
#                                 if child != 0 and state[mouse,child,True] != 1:
#                                     all_lose = False
#                                     break
#                             if all_lose:
#                                 state[mouse,parent,False] = 1
#                                 q.append((mouse,parent,False))
#             else:
#                 if score == 1:
#                     for parent in graph[mouse]:
#                         if state[parent,cat,True] == 0:
#                             state[parent,cat,True] = 1
#                             q.append((parent,cat,True))
#                 else:
#                     for parent in graph[mouse]:
#                         if state[parent,cat,True] == 0:
#                             all_lose = True
#                             for child in graph[parent]:
#                                 if state[child,cat,False] != 2:
#                                     all_lose = False
#                                     break
#                             if all_lose:
#                                 state[parent,cat,True] = 2
#                                 q.append((parent,cat,True))
#         return state[1,2,True]



# from collections import deque, defaultdict

# class Solution:
#     def catMouseGame(self, graph: List[List[int]]) -> int:
#         n = len(graph)
#         q = deque()
#         state = defaultdict(int)
#         degree = defaultdict(int)
#         for mouse in range(1,n):
#             for cat in range(1,n):
#                 degree[mouse,cat,True] = len(graph[mouse])
#                 degree[mouse,cat,False] = len(graph[cat]) - (0 in graph[cat])
#         for cat in range(1,n):
#             state[0,cat,True] = 1
#             state[0,cat,False] = 1 
#             q.append((0,cat,True))
#             q.append((0,cat,False))
#         for pos in range(1,n):
#             state[pos,pos,True] = 2
#             state[pos,pos,False] = 2
#             q.append((pos,pos,True))
#             q.append((pos,pos,False))
#         while q:
#             mouse, cat, mouseMove = q.popleft()
#             score = state[mouse,cat,mouseMove]
#             if mouseMove:
#                 if score == 2:
#                     for parent in graph[cat]:
#                         if parent != 0 and state[mouse,parent,False] == 0:
#                             state[mouse,parent,False] = 2
#                             q.append((mouse,parent,False))
#                 else:
#                     for parent in graph[cat]:
#                         if parent != 0 and state[mouse,parent,False] == 0:
#                             degree[mouse,parent,False] -= 1
#                             if degree[mouse,parent,False] == 0:
#                                 state[mouse,parent,False] = 1
#                                 q.append((mouse,parent,False))
#             else:
#                 if score == 1:
#                     for parent in graph[mouse]:
#                         if state[parent,cat,True] == 0:
#                             state[parent,cat,True] = 1
#                             q.append((parent,cat,True))
#                 else:
#                     for parent in graph[mouse]:
#                         if state[parent,cat,True] == 0:
#                             degree[parent,cat,True] -= 1
#                             if degree[parent,cat,True] == 0:
#                                 state[parent,cat,True] = 2
#                                 q.append((parent,cat,True))
#         return state[1,2,True]

class Solution(object):
    def catMouseGame(self, graph):
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]

