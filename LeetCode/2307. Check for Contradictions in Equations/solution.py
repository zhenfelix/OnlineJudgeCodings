class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        g = defaultdict(list)
        for (a, b), r in zip(equations,values):
            g[a].append((b,1/r))
            g[b].append((a,r))
        dp = dict()

        def dfs(cur, v):
            if cur in dp:
                return
            dp[cur] = v 
            for nxt, r in g[cur]:
                dfs(nxt, v*r)
            return

        for a, b in equations:
            dfs(a, 1)
        # print(dp)
        delta = 10**-5
        for (a, b), r in zip(equations,values):
            if abs(dp[a]-dp[b]*r) > delta:
                return True
        return False 



class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:

        edges = defaultdict(set)
        for j,(x,y) in enumerate(equations):
            edges[x].add((y,values[j])) 
            edges[y].add((x,1/values[j]))  #图中的边一定要成对添加
        val = {}
        ans = False #初始默认没有矛盾

        def dfs(node,v):
            nonlocal ans
            if ans: #已经有矛盾就不浪费时间了
                return
            if node in val:
                if abs(val[node]/v-1.)>1e-5: #题目明确说不超过1e-5视为相同值，由于判断是否矛盾本身也是根据比值关系，因此这里用相对误差不超过1e-5来判断
                    ans=True
                return #搜过的点，不管有没有矛盾，都应直接return，否则程序就会死循环         
            val[node]=v
            for nei,rat in edges[node]:
                dfs(nei,v/rat)
        
        for x,y in equations:
            if x not in val: # 如果x还没有值，y也一定没有，这时说明遇到了一个新的连通分量
                dfs(x,1.)
        return ans


# 作者：v5qYY4Q65w
# 链接：https://leetcode.cn/problems/check-for-contradictions-in-equations/solution/jian-wu-xiang-tu-shen-du-you-xian-sou-su-9thq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。