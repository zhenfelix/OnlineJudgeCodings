# class Solution:
#     def respace(self, dictionary: List[str], sentence: str) -> int:
#         dictionary = set(dictionary)
#         rn = len(sentence)
#         dp = [0]
#         for i in range(n):
#             dp.append(dp[-1]+1)
#             cur = ""
#             for j in range(i+1)[::-1]:
#                 cur = sentence[j]+cur
#                 if cur in dictionary:
#                     dp[-1] = min(dp[-1],dp[j])
#                 else:
#                     dp[-1] = min(dp[-1],dp[j]+len(cur))
#         return dp[-1]


class Node:
    def __init__(self):
        self.child = {}
        self.idx = -1
        self.fail = None

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,idx,word):
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node()
            cur = cur.child[w]
        cur.idx = idx
        return

    def automata(self):
        q = deque()
        root = self.root
        root.fail = root
        for w in root.child:
            root.child[w].fail = root
            q.append(root.child[w])
        while q:
            cur = q.popleft()
            for w in cur.child:
                f = cur.fail
                while w not in f.child and f != root:
                    f = f.fail
                if w in f.child: f = f.child[w]
                cur.child[w].fail = f
                # cur.child[w].idx += f.idx
                q.append(cur.child[w])
        return

    def show(self):
        q = deque()
        root = self.root
        q.append(root)
        while q:
            cur = q.popleft()
            print(cur,cur.idx,cur.child,cur.fail)
            for w in cur.child:
                q.append(cur.child[w])
        return




class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:

    # def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        T = Trie()
        for i, word in enumerate(dictionary):
            T.insert(i,word)
        T.automata()
        # T.show()
        dp = [0]
        cur = T.root
        for i, ch in enumerate(sentence):
            dp.append(dp[-1]+1)
            while ch not in cur.child and cur != T.root:
                cur = cur.fail
            if ch in cur.child: cur = cur.child[ch]
            # print(i,cur,cur.child,cur.idx)
            p = cur
            while p != T.root:
                if p.idx != -1: 
                    idx = p.idx
                    dp[-1] = min(dp[-1],dp[i-len(dictionary[idx])+1])
                p = p.fail
            
            # for idx in cur.idx:
            #     dp[-1] = min(dp[-1],dp[i-len(dictionary[idx])+1])
        return dp[-1]