class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neib = defaultdict(list)
        n = len(adjacentPairs) + 1
        for a, b in adjacentPairs:
            neib[a].append(b)
            neib[b].append(a)
        cur = None
        for x in neib:
            if len(neib[x]) == 1:
                cur = x
                break
        ans = [cur]
        visited = set()
        visited.add(cur)
        while len(ans) < n:
            for nxt in neib[cur]:
                if nxt not in visited:
                    break
            cur = nxt
            ans.append(cur)
            visited.add(cur)
        return ans 