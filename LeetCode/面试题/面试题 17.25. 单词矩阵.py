class Node:
    def __init__(self):
        self.isWord = False
        self.child = {}
        self.potential = set()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node()
            cur = cur.child[w]
            cur.potential.add(len(word))
        cur.isWord = True
        return



class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        myTrie = Trie()
        len2word = defaultdict(list)
        for word in words:
            myTrie.insert(word)
            len2word[len(word)].append(word)
        area, res, all_set = 0, [], set(len2word)
        # candidate = []
        def dfs(state, width, depth, candidate):
            nonlocal area, res
            if width*depth > area and all(x.isWord for x in state):
                area = width*depth
                # res = candidate[:]
                res = candidate
            for word in len2word[width]:
                nxt = []
                for cur, ch in zip(state,word):
                    if ch not in cur.child:
                        break
                    nxt.append(cur.child[ch])
                nxt_potential = reduce(lambda x,y: x&y, [x.potential for x in nxt], all_set)
                # if len(nxt) == width:
                if len(nxt) == width and nxt_potential and max(nxt_potential)*width > area:
                    # candidate.append(word)
                    dfs(nxt, width, depth+1, candidate+[word])
                    # candidate.pop()
            return

        mxlen = max(len2word)
        for w in sorted(len2word)[::-1]:
            # if w*mxlen < area:
            #     break
            dfs([myTrie.root]*w, w, 0, [])
        return res












class Node:
    def __init__(self):
        self.isWord = False
        self.child = {}
        # self.potential = set()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node()
            cur = cur.child[w]
            # cur.potential.add(len(word))
        cur.isWord = True
        return



class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        myTrie = Trie()
        len2word = defaultdict(list)
        for word in words:
            myTrie.insert(word)
            len2word[len(word)].append(word)
        area, res, all_set = 0, [], set(len2word)
        # candidate = []
        def dfs(state, width, depth, candidate):
            nonlocal area, res
            if width*depth > area and all(x.isWord for x in state):
                area = width*depth
                # res = candidate[:]
                res = candidate
            for word in len2word[width]:
                nxt = []
                for cur, ch in zip(state,word):
                    if ch not in cur.child:
                        break
                    nxt.append(cur.child[ch])
                # nxt_potential = reduce(lambda x,y: x&y, [x.potential for x in nxt], all_set)
                if len(nxt) == width:
                # if len(nxt) == width and nxt_potential and max(nxt_potential)*width > area:
                    # candidate.append(word)
                    dfs(nxt, width, depth+1, candidate+[word])
                    # candidate.pop()
            return

        mxlen = max(len2word)
        for w in sorted(len2word)[::-1]:
            if w*mxlen < area:
                break
            dfs([myTrie.root]*w, w, 0, [])
        return res

