class Solution:
    def oddString(self, words: List[str]) -> str:
        n, m = len(words), len(words[0])
        mat = [[-1]*(m-1) for _ in range(n)]
        cc = Counter()
        for i in range(n):
            for j in range(m-1):
                mat[i][j] = ord(words[i][j+1])-ord(words[i][j])
            cc[tuple(mat[i])] += 1
        for i in range(n):
            for j in range(m-1):
                mat[i][j] = ord(words[i][j+1])-ord(words[i][j])
            if cc[tuple(mat[i])] == 1:
                return words[i]
        return ""


class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(list)
        for s in words:
            d[tuple(ord(x) - ord(y) for x, y in pairwise(s))].append(s)
        x, y = d.values()
        return x[0] if len(x) == 1 else y[0]


作者：endlesscheng
链接：https://leetcode.cn/problems/odd-string-difference/solution/ha-xi-biao-by-endlesscheng-k6f5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。