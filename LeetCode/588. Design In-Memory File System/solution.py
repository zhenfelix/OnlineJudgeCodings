class FileSystem:

    def __init__(self):
        self.contents = {}
        self.tree = Trie()
        

    def ls(self, path: str) -> List[str]:
        if path in self.contents:
            # print(path.split('/'))
            return [path.split('/')[-1]]
        return self.tree.read(path.split('/'))
        

    def mkdir(self, path: str) -> None:
        self.tree.write(path.split('/'))
        return
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.contents:
            self.mkdir(filePath)
            self.contents[filePath] = ""
        self.contents[filePath] = self.contents[filePath] + content
        

    def readContentFromFile(self, filePath: str) -> str:
        return self.contents[filePath]
        
class Trie:
    """docstring for Trie"""
    def __init__(self):
        self.root = Node()

    def read(self, path):
        cur = self.root
        if path[1]:
            for name in path[1:]:
                cur = cur.nxt[name]
        
        if not cur.nxt:
            # return [path[-1]] if path[-1] else []
            return []
        return sorted(cur.nxt.keys())

    def write(self, path):
        cur = self.root
        for name in path[1:]:
            if name not in cur.nxt:
                cur.nxt[name] = Node()
            cur = cur.nxt[name]
        return

class Node:

    def __init__(self):
        self.nxt = {}

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)