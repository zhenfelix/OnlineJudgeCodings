class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        s = list(s)
        tree = [0] * n

        def update(i, delta):
            i += 1
            while i < n:
                tree[i] += delta
                i += i & (-i)

        def query(i):
            i += 1
            res = 0
            while i > 0:
                res += tree[i]
                i -= i & (-i)
            return res

        for i in range(n - 1):
            if s[i] == s[i+1]:
                update(i, 1)

        ans = []
        for qq in queries:
            type = qq[0]
            if type == 1:
                idx = qq[1]
                for k in (idx - 1, idx):
                    if 0 <= k < n - 1 and s[k] == s[k+1]:
                        update(k, -1)
                
                s[idx] = 'B' if s[idx] == 'A' else 'A'
                
                for k in (idx - 1, idx):
                    if 0 <= k < n - 1 and s[k] == s[k+1]:
                        update(k, 1)
            else:
                l, r = qq[1:]
                ans.append(query(r - 1) - query(l - 1))
                
        return ans