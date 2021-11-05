class FileSystem:

    def __init__(self):
        self.root = {'val':-1, 'children': defaultdict(dict)}

    def _iter(self, cur, path):
        for p in path:
            if p not in cur['children']:
                return False
            cur = cur['children'][p]
        return cur


    def createPath(self, path: str, value: int) -> bool:
        path = path.split('/')[1:]
        cur = self._iter(self.root, path[:-1])
        if not cur or path[-1] in cur['children']:
            return False
        cur['children'][path[-1]] = {'val': value, 'children': defaultdict(dict)}
        return True

    def get(self, path: str) -> int:
        path = path.split('/')[1:]
        cur = self._iter(self.root, path)
        if not cur:
            return -1
        return cur['val']



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)