class Node:
    def __init__(self):
        self.mp = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        p = self.root
        for w in word:
            if w not in p.mp:
                p.mp[w] = Node()
            p = p.mp[w]
        p.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)
        # p = self.root
        def dfs(idx, p):
            if idx == n:
                return p.isEnd == True
            if word[idx] == '.':
                for k, v in p.mp.items():
                    if dfs(idx+1, v):
                        return True
                return False
            if word[idx] not in p.mp:
                return False
            return dfs(idx+1, p.mp[word[idx]])
        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)