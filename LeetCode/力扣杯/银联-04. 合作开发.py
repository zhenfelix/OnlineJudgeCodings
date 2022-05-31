class Solution:
    def coopDevelop(self, skills: List[List[int]]) -> int:
        cnt = Counter()
        eq, cont = 0, 0
        sz = len(skills)
        for sk in skills:
            cnt[tuple(sk)] += 1
        for sk in skills:
            n = len(sk)
            for s in range(1,(1<<n)-1):
                candidate = []
                for i in range(n):
                    if (s>>i)&1:
                        candidate.append(sk[i])
                cont += cnt[tuple(candidate)]
            eq += cnt[tuple(sk)]-1
        return (sz*(sz-1)//2-cont-eq//2)%(10**9+7)


class Solution:
    def coopDevelop(self, skills: List[List[int]]) -> int:
        cnt = Counter()
        eq, cont = 0, 0
        sz = len(skills)
        for sk in skills:
            cnt[tuple(sk)] += 1

        def dfs(sks, idx, candidate):
            if idx == len(sks):
                if 0 < len(candidate) < len(sks):
                    yield tuple(candidate)
                return
            yield from dfs(sks, idx+1, candidate)
            yield from dfs(sks, idx+1, candidate+[sks[idx]])
            return

        for sk in skills:
            n = len(sk)
            for candidate in dfs(sk,0,[]):
                cont += cnt[candidate]
            eq += cnt[tuple(sk)]-1
        return (sz*(sz-1)//2-cont-eq//2)%(10**9+7)
