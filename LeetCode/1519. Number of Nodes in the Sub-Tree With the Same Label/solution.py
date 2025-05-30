class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        cnt = [Counter() for _ in range(n)]
        def dfs(node: int, parent: int):
            cnt[node][labels[node]] += 1
            for child in g.get(node, []):
                if child != parent:
                    dfs(child, node)
                    for ch in ascii_lowercase:
                        cnt[node][ch] += cnt[child][ch]
            ans[node] = cnt[node][labels[node]]
            return 
        
        g, ans = defaultdict(list), [0] * n
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]
        dfs(0, -1)
        return ans 

# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
#         def dfs(node: int, parent: int):
#             cnt = Counter(labels[node])
#             for child in g.get(node, []):
#                 if child != parent:
#                     cnt += dfs(child, node)
#             ans[node] = cnt[labels[node]]
#             return cnt
        
#         g, ans = defaultdict(list), [0] * n
#         for a, b in edges:
#             g[a] += [b]
#             g[b] += [a]
#         dfs(0, -1)
#         return ans    