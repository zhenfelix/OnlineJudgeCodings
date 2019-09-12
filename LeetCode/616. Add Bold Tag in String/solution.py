# class TrieNode():
#     def __init__(self):
#         self.child = {}
#         self.word = False

# class Solution:
#     def addBoldTag(self, s: str, dict: List[str]) -> str:
#         root = TrieNode()
#         for word in dict:
#             cur = root
#             for w in word:
#                 if w not in cur.child:
#                     cur.child[w] = TrieNode()
#                 cur = cur.child[w]
#             cur.word = True
        
#         pairs = []
#         for i, _ in enumerate(s):
#             pos, cur = i, root
#             while pos < len(s) and s[pos] in cur.child:
#                 cur = cur.child[s[pos]]
#                 pos += 1
#             if pos > i and cur.word:
#                 pairs.append([i,pos])
        
#         new_pairs = []
#         for p in pairs:
#             if new_pairs and new_pairs[-1][-1] >= p[0]:
#                 new_pairs[-1][-1] = max(new_pairs[-1][-1], p[1])
#             else:
#                 new_pairs += [p]
                
#         res = ""
#         start = 0
#         for p in new_pairs:
#             res += s[start:p[0]]
#             res += '<b>'+s[p[0]:p[1]]+'</b>'
#             start = p[1]
#         res += s[start:]
#         return res

# class Solution:
#     def addBoldTag(self, s: str, dict: List[str]) -> str:
#         lookup = set()
#         for d in dict:
#             left = 0
#             while True:
#                 loc = s.find(d, left)#kmp api in find function
#                 if loc == -1:
#                     break
#                 for i in range(loc, loc + len(d)):
#                     lookup.add(i)
#                 left = loc + 1
#         res = ""
#         i = 0
#         while i < len(s):
#             left = i
#             while i < len(s) and i in lookup:
#                 i += 1
#             # print(left, i)
#             if left == i:
#                 res += s[i]
#                 i += 1
#             else:
#                 res += "<b>"
#                 for j in range(left, i):
#                     res += s[j]
#                 res += "</b>"
#         return res

from collections import deque

class TrieNode():
    def __init__(self):
        self.child = {}
        self.idx = -1
        self.fail = None


class Automaton(object):
    """docstring for Automata"""
    def __init__(self, words):
        self.root = TrieNode()
        for i, word in enumerate(words):
            self.insert(word, i)
        self.build()

    def insert(self, word, idx):
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode()
            cur = cur.child[w]
        cur.idx = idx

    def build(self):
        q = deque()
        # for i in range(26):
        #   ch = chr(ord('a')+i)
        #   if ch not in self.root.child:
        #       self.root.child[ch] = self.root

        for ch, node in self.root.child.items():
            node.fail = self.root
            q.append(node)

        while q:
            front = q.popleft()
            for ch, node in front.child.items():
                fail = front.fail
                while ch not in fail.child:
                    if fail == self.root:
                        fail.child[ch] = self.root
                        break
                    fail = fail.fail
                node.fail = fail.child[ch]
                q.append(node)

    def next(self, cur, ch):
        while ch not in cur.child:
            if cur == self.root:
                cur.child[ch] = cur
                break
            cur = cur.fail
        return cur.child[ch]
        
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        machine = Automaton(dict)       
        pairs = []
        curState = machine.root
        for i, ch in enumerate(s):
            curState = machine.next(curState, ch)
            if curState.idx != -1:
                right = i + 1
                left = right - len(dict[curState.idx])
                pairs.append([left, right])
        
        new_pairs = []
        for p in pairs:
            if new_pairs and new_pairs[-1][-1] >= p[0]:
                new_pairs[-1][-1] = max(new_pairs[-1][-1], p[1])
            else:
                new_pairs += [p]
                
        res = ""
        start = 0
        for p in new_pairs:
            res += s[start:p[0]]
            res += '<b>'+s[p[0]:p[1]]+'</b>'
            start = p[1]
        res += s[start:]
        return res



# from collections import deque

# # class TrieNode():
# #    def __init__(self):
# #        self.child = {}
# #        self.idx = -1
# #        self.fail = None


# class Automaton(object):
#     """docstring for Automata"""
#     def __init__(self, words):
#         self.g = {}
#         self.f = {}
#         self.idx = {}
#         self.alphabet = set()
#         states = 1
#         for i, word in enumerate(words):
#             cur = 0
#             for w in word:
#                 if w not in self.alphabet:
#                     self.alphabet.add(w)
#                 if (cur,w) not in self.g:
#                     self.g[cur,w] = states
#                     states += 1
#                 cur = self.g[cur,w]
#             self.idx[cur] = i 
#         self.build()

#     # def insert(self, word, idx):
#     #    cur = self.root
#     #    for w in word:
#     #        if w not in cur.child:
#     #            cur.child[w] = TrieNode()
#     #        cur = cur.child[w]
#     #    cur.idx = idx

#     def build(self):
#         q = deque()
#         # for i in range(26):
#         #   ch = chr(ord('a')+i)
#         #   if ch not in self.root.child:
#         #      self.root.child[ch] = self.root

#         for ch in self.alphabet:
#             if (0,ch) in self.g:
#                 state = self.g[0,ch]
#                 self.f[state] = 0
#                 q.append(state)

#         while q:
#             front = q.popleft()
#             for ch in self.alphabet:
#                 if (front,ch) in self.g:
#                     state = self.g[front,ch]
#                     fail = self.f[front]
#                     while (fail,ch) not in self.g:
#                         if fail == 0:
#                             self.g[fail,ch] = 0
#                             break
#                         fail = self.f[fail]
#                     self.f[state] = self.g[fail,ch]
#                     q.append(state)

#     def next(self, cur, ch):
#         while (cur,ch) not in self.g:
#             if cur == 0:
#                 self.g[cur,ch] = 0
#                 break
#             cur = self.f[cur]
#         return self.g[cur,ch]
        
# class Solution:
#     def addBoldTag(self, s: str, dict: List[str]) -> str:
#         machine = Automaton(dict)      
#         pairs = []
#         curState = 0
#         for i, ch in enumerate(s):
#             curState = machine.next(curState, ch)
#             if curState in machine.idx:
#                 right = i + 1
#                 left = right - len(dict[machine.idx[curState]])
#                 pairs.append([left, right])
        
#         new_pairs = []
#         for p in pairs:
#             if new_pairs and new_pairs[-1][-1] >= p[0]:
#                 new_pairs[-1][-1] = max(new_pairs[-1][-1], p[1])
#             else:
#                 new_pairs += [p]
                
#         res = ""
#         start = 0
#         for p in new_pairs:
#             res += s[start:p[0]]
#             res += '<b>'+s[p[0]:p[1]]+'</b>'
#             start = p[1]
#         res += s[start:]
#         return res
# 超时了