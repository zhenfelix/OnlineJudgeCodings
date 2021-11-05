class Solution:
    def volunteerDeployment(self, finalCnt: List[int], totalNum: int, edges: List[List[int]], plans: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def calc(x):
            cnt = [x]+finalCnt
            for op, idx in plans[::-1]:
                if op == 1:
                    cnt[idx] *= 2
                elif op == 2:
                    for nxt in graph[idx]:
                        cnt[nxt] -= cnt[idx]
                else:
                    for nxt in graph[idx]:
                        cnt[nxt] += cnt[idx]
            return cnt

        lo, hi = 0, totalNum*10
        fmi = sum(calc(lo))-totalNum
        fmx = sum(calc(hi))-totalNum
        while lo <= hi:
            mid = (lo+hi)//2
            cur = calc(mid)
            if (sum(cur)-totalNum)*fmx > 0:
                hi = mid-1
            else:
                lo = mid+1
        return calc(hi)






class Solution:
    def volunteerDeployment(self, finalCnt: List[int], totalNum: int, edges: List[List[int]], plans: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def calc(x):
            cnt = [x]+finalCnt
            for op, idx in plans[::-1]:
                if op == 1:
                    cnt[idx] *= 2
                elif op == 2:
                    for nxt in graph[idx]:
                        cnt[nxt] -= cnt[idx]
                else:
                    for nxt in graph[idx]:
                        cnt[nxt] += cnt[idx]
            return cnt
        n = len(finalCnt)+1
        k = [1] + [0]*(n-1)
        b = [0] + finalCnt
        for op, idx in plans[::-1]:
            if op == 1:
                k[idx] *= 2
                b[idx] *= 2
            elif op == 2:
                for nxt in graph[idx]:
                    k[nxt] -= k[idx]
                    b[nxt] -= b[idx]
            else:
                for nxt in graph[idx]:
                    k[nxt] += k[idx]
                    b[nxt] += b[idx]
        ks = sum(k)
        bs = sum(b)
        x = (totalNum-bs)//ks
        return [kk*x+bb for kk, bb in zip(k,b)]


