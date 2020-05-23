class Node:
    def __init__(self):
        self.child = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node()
            cur = cur.child[w]
        cur.isWord = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        T = Trie()
        for word in words:
            T.insert(word)
        res, memo = "", {}
        def dfs(s):
            if s in memo: return memo[s]
            n, cur = len(s), T.root
            for i in range(n):
                if s[i] not in cur.child:
                    memo[s] = 0
                    return 0
                cur = cur.child[s[i]]
                if cur.isWord and dfs(s[i+1:]):
                    memo[s] = 2
                    return 2
            memo[s] = 1 if cur.isWord else 0
            return memo[s]

        for word in sorted(words, key=lambda x: (-len(x),x)):
            if dfs(word) == 2 and len(word) > len(res): return word
        return res





class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda x: (-len(x), x))
        # 假设无重复
        words_set = set(words)

        def func(word, from_idx, word_len):
            if word[from_idx:] in words_set and from_idx > 0:
                return True
            for idx in range(from_idx+1, word_len):
                if word[from_idx:idx] in words_set and func(word, idx, word_len):
                    return True
            return False
        
        for word in words:
            if func(word, 0, len(word)):
                return word
        
        return ''