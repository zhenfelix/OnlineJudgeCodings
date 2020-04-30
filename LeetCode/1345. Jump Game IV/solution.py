class Solution:
    # def minJumps(self, arr: List[int]) -> int:
    #     g = defaultdict(list)
    #     for i, a in enumerate(arr):
    #         g[a].append(i)
    #     visited = set([0])
    #     q = deque([0])
    #     step = 0
    #     while q:
    #         n = len(q)
    #         for _ in range(len(q)):
    #             cur = q.popleft()
    #             if cur == len(arr)-1:
    #                 return step
    #             for nxt in [-1,1]:
    #                 nxt += cur
    #                 if 0 <= nxt < len(arr) and nxt not in visited:
    #                     visited.add(nxt)
    #                     q.append(nxt)
    #             while g[arr[cur]]:
    #                 nxt = g[arr[cur]].pop()
    #                 if nxt not in visited:
    #                     visited.add(nxt)
    #                     q.append(nxt)
    #         step += 1
    #     return -1
    
    def minJumps(self, A):
        indices = collections.defaultdict(list)
        for i, a in enumerate(A):
            indices[a].append(i)
        done, now = {-1}, {0}
        for steps in itertools.count():
            done |= now
            if len(A) - 1 in done:
                return steps
            now = {j for i in now for j in [i-1, i+1] + indices.pop(A[i], [])} - done
