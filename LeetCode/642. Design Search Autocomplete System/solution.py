class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.candidates = []
        self.idx = -1

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences = sentences
        self.times = times
        self.cur = self.root = Node()
        self.path = []
        for i, s in enumerate(sentences):
            for ch in s:
                self._travel(ch)
            self.cur.idx = i 
            self._update()

    def _travel(self, ch):
        self.path.append((self.cur,ch))
        self.cur = self.cur.child[ch]

    def _update(self):
        self.path.append((self.cur,''))
        while self.path:
            self.cur, _ = self.path.pop()
            idx = self.cur.idx
            tmp = [] if idx == -1 else [(-self.times[idx],'',0,idx)]
            for ch, child in self.cur.child.items():
                for rank, idx in enumerate(child.candidates):
                    tmp.append((-self.times[idx],ch,rank,idx))
            tmp.sort()
            self.cur.candidates = [idx for _,_,_,idx in tmp[:3]]

    def _debug(self):
        if self.path:
            self._path = self.path[:]
            print("before update")
        else:
            print("after update")
        for cur, ch in self._path:
            print(ch,cur.candidates, self.sentences, self.times)
        

    def input(self, c: str) -> List[str]:
        ans = []
        if c != '#':
            self._travel(c)
            return [self.sentences[i] for i in self.cur.candidates]
        else:
            # self._debug()
            if self.cur.idx == -1:
                self.cur.idx = len(self.sentences)
                self.sentences.append(''.join([ch for _, ch in self.path]))
                self.times.append(0)
            self.times[self.cur.idx] += 1
            self._update()
            # self._debug()
            return []
            
            
            
            
            
        




# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)