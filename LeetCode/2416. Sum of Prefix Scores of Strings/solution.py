class Node:
    __slots__ = 'son', 'ids', 'score'

    def __init__(self):
        self.son = defaultdict(Node)
        self.ids = []
        self.score = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Node()
        for i, word in enumerate(words):
            cur = root
            for c in word:
                cur = cur.son[c]
                cur.score += 1  # 更新所有前缀的分数
            cur.ids.append(i)

        ans = [0] * len(words)
        def dfs(node: Node, sum: int) -> None:
            sum += node.score  # 累加分数，即可得到答案
            for i in node.ids:
                ans[i] = sum
            for child in node.son.values():
                if child:
                    dfs(child, sum)
        dfs(root, 0)
        return ans


作者：endlesscheng
链接：https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/solution/by-endlesscheng-ghfr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Node:
    def __init__(self):
        self.children = dict()
        self.cnt = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Node()
        def add(wd):
            cur = root
            for ch in wd:
                if ch not in cur.children:
                    cur.children[ch] = Node()
                cur = cur.children[ch]
                cur.cnt += 1

        def query(wd):
            cur = root
            score = 0
            for ch in wd:
                cur = cur.children[ch]
                score += cur.cnt
            return score

        for wd in words:
            add(wd)
        n = len(words)
        ans = [0]*n 
        for i, wd in enumerate(words):
            ans[i] = query(wd)
        return ans 
