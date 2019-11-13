class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n > m:
            n, m = m, n
        state = [0]*n

        def dfs(cnt):
            if cnt >= res[0]:
                return
            s = min(range(n), key = lambda x: state[x])
            if state[s] == m:
                res[0] = cnt
                return
            e = s
            while e < n and state[e] == state[s] and e-s+1 <= m-state[s]:
                e += 1
            for j in range(s,e)[::-1]:
                sz = j-s+1
                for i in range(s,j+1):
                    state[i] += sz
                dfs(cnt+1)
                for i in range(s,j+1):
                    state[i] -= sz
            return

        res = [m*n]
        dfs(0)
        return res[0]