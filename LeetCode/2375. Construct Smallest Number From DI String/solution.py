# class Solution:
#     def smallestNumber(self, pattern: str) -> str:
#         n = len(pattern) + 1
#         for p in itertools.permutations(range(1, n + 1)):
#             t = list(p)
#             valid = True
#             for i in range(n - 1):
#                 if (p[i + 1] > p[i] and pattern[i] == 'D') or (p[i + 1] < p[i] and pattern[i] == 'I'):
#                     valid = False
#                     break
#             if valid:
#                 return ''.join(map(str, p))
#         return ''

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = ""
        def dfs(path):
            nonlocal ans 
            if len(path) == n+1:
                ans = ''.join(map(str,path))
                return True
            j = len(path)-1
            # print(path)
            for i in range(1,10):
                
                if (not path) or (((pattern[j] == 'I' and path[-1] < i) or (pattern[j] == 'D' and path[-1] > i)) and i not in path):
                    path.append(i)
                    if dfs(path):
                        return True
                    path.pop()
            return False
        dfs([])
        return ans 


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1
        degree = [0]*n 
        g = [[] for _ in range(n)]
        ans = ['']*n 
        for i, ch in enumerate(pattern):
            if ch == 'I':
                degree[i+1] += 1
                g[i].append(i+1)
            else:
                degree[i] += 1
                g[i+1].append(i)
        q = deque()
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
        mx = 1 
        while q:
            cur = q.popleft()
            ans[cur] = str(mx)
            mx += 1
            for nxt in g[cur][::-1]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.appendleft(nxt)
        return ''.join(ans)


作者：zhenfisher
链接：https://leetcode.cn/problems/construct-smallest-number-from-di-string/solution/tuo-bu-by-zhenfisher-52g2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。