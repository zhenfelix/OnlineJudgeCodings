import collections

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            p = root
            for w in word:
                p = p.children[w]
            p.isWord = True
        
        ans = []
        n = len(board)
        if n == 0:
            return ans
        m = len(board[0])
        dx, dy = [1,-1,0,0], [0,0,-1,1]
        def dfs(i, j, cur, path):
            if cur.isWord:
                ans.append(path)
                cur.isWord = False
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == "#":
                return
            # for ch, v in cur.children.items():
            #     if board[i][j] == ch:
            #         for t in range(4):
            #             board[i][j] = board[i][j].upper()
            #             dfs(i+dx[t], j+dy[t], v, path+ch)
            #             board[i][j] = board[i][j].lower()
            if board[i][j] in cur.children:
                ch = board[i][j]
                board[i][j] = "#"
                for t in range(4):
                    dfs(i+dx[t], j+dy[t], cur.children[ch], path+ch)
                board[i][j] = ch
            return
        
        for x in range(n):
            for y in range(m):
                dfs(x, y, root, "")
        
        return ans
        