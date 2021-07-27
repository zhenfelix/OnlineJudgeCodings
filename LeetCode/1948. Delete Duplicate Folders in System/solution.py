from hashlib import sha256
from sortedcontainers import SortedDict
class Node:
    def __init__(self, val='', idx=-1):
        self.val = val
        self.idx = idx
        self.merkle = ''
        self.children = SortedDict()


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, path, idx):
        cur = self.root
        for ch in path:
            if ch not in cur.children:
                cur.children[ch] = Node(ch, idx)
            cur = cur.children[ch]
        return cur

class Solution:
    


    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        paths.sort(key = lambda x: len(x))
        n = len(paths)
        hash_arr = [0]*n 
        mp = [None]*n 
        tree = Trie()
        for i, path in enumerate(paths):
            mp[i] = tree.insert(path,i)
        


        def hash_(x):
            S = sha256()
            
            S.update(x.encode('utf-8'))
            return S.hexdigest()

        def merkle(node):
            if node.children:
                node.merkle = hash_('#'.join([merkle(c) for c in node.children.values()]))
            hash_arr[node.idx] = node.merkle
            return hash_(node.merkle+'#'+node.val+'#')

        merkle(tree.root)
        cc = Counter(hash_arr)
        # print(paths,cc)
        # print(hash_arr)
        todo = set()

        def remove(cur):
            todo.add(cur.idx)
            for ch, nxt in cur.children.items():
                remove(nxt)
            return 

        res = []
        for i, path in enumerate(paths):
            if i in todo:
                continue
            if cc[hash_arr[i]] > 1 and mp[i].children:
                remove(mp[i])
                continue
            res.append(path[:])
                
        return res