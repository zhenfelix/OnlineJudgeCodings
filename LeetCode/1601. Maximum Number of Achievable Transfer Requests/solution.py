class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        check = [-float('inf')]*(1<<m)
        for i in range(1<<m):
            flow, cnt = [0]*n, 0
            for j in range(m):
                if i & (1<<j):
                    cnt += 1
                    a, b = requests[j]
                    flow[a] -= 1
                    flow[b] += 1
            if all(x == 0 for x in flow):
                check[i] = cnt
        # def dfs(idx, state):
        #     if idx == n:
        #         return check[state]
        #     return max(dfs(idx+1,state), dfs(idx+1,state|(1<<idx)))
        return max(check)

    def maximumRequests(self, n, req):
        for k in range(len(req), 0, -1):
            for c in itertools.combinations(range(len(req)), k):
                degree = [0] * n
                for i in c:
                    degree[req[i][0]] -= 1
                    degree[req[i][1]] += 1
                if not any(degree):
                    return k
        return 0