class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        g = defaultdict(list)
        mx = [[(-1,-1)]*3 for _ in range(n)]
        for a, b in edges:
            heapq.heappush(mx[a],(scores[b],b))
            heapq.heappop(mx[a])
            heapq.heappush(mx[b],(scores[a],a))
            heapq.heappop(mx[b])
        ans = -1
        # print(mx)
        for a, b in edges:
            for sa, ia in mx[a]:
                for sb, ib in mx[b]:
                    if ia != ib and ia not in [-1,b] and ib not in [-1,a]:
                        # print(a,b,ia,ib,scores[a]+scores[b]+sa+sb)
                        ans = max(ans, scores[a]+scores[b]+sa+sb)
        return ans



class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = [[] for _ in range(len(scores))]
        for x, y in edges:
            g[x].append((scores[y], y))
            g[y].append((scores[x], x))
        for i, vs in enumerate(g):
            g[i] = nlargest(3, vs)

        # 下面这一段可以简写成一行，为了可读性这里就不写了
        ans = -1
        for x, y in edges:
            for (score_a, a), (score_b, b) in product(g[x], g[y]):
                if y != a != b != x:
                    ans = max(ans, score_a + scores[x] + scores[y] + score_b)
        return ans


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/maximum-score-of-a-node-sequence/solution/by-endlesscheng-dt8h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。