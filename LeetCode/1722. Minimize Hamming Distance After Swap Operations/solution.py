class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
            return
        for a, b in allowedSwaps:
            union(a,b)
        left, right = defaultdict(Counter), defaultdict(Counter)
        for i in range(n):
            left[find(i)][source[i]] += 1
            right[find(i)][target[i]] += 1
        cnt = 0
        # print(left,right)
        # print([find(i) for i in range(n)])
        for k in left:
            for k2 in left[k]:
                cnt += max(0,left[k][k2]-right[k][k2])
            # cnt += len(left[k])-len(left[k]&right[k])
        return cnt

