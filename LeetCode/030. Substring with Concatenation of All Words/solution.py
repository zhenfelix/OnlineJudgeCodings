# from collections import deque
# from collections import Counter

# class TrieNode():
#     def __init__(self):
#         self.child = {}
#         self.fail = None
#         self.pattern = None
        
# class Automaton():
#     def __init__(self, words):
#         self.root = TrieNode()
#         for i, word in enumerate(words):
#             self.insert(word, words[i])
#         self.build()
            
#     def insert(self, word, pattern):
#         cur = self.root
#         for w in word:
#             if w not in cur.child:
#                 cur.child[w] = TrieNode()
#             cur = cur.child[w]
#         cur.pattern = pattern
        
#     def build(self):
#         q = deque()
#         for ch in self.root.child:
#             node = self.root.child[ch]
#             node.fail = self.root
#             q.append(node)
#         while q:
#             front = q.popleft()
#             for ch in front.child:
#                 fail = front.fail
#                 while ch not in fail.child:
#                     if fail == self.root:
#                         fail.child[ch] = fail
#                         break
#                     fail = fail.fail
#                 front.child[ch].fail = fail.child[ch]
#                 q.append(front.child[ch])
    
#     def next(self, cur, ch):
#         while ch not in cur.child:
#             if cur == self.root:
#                 cur.child[ch] = self.root
#                 break
#             cur = cur.fail
#         return cur.child[ch]
    
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if not words:
#             return []
#         machine = Automaton(words)
#         state = machine.root
#         n, m = len(words), len(words[0])
#         arr = [None]*len(s)
#         cc = Counter(words)
#         res = []
        
#         for i, ch in enumerate(s):
#             state = machine.next(state,ch)
#             pattern = state.pattern
#             if pattern:
#                 arr[i-m+1] = pattern
                
#         for i in range(m):
#             mp = Counter()
#             left, right = 0, 0
#             while i + right*m < len(s):
#                 if arr[i+right*m]:
#                     mp[arr[i+right*m]] += 1
#                     while left <= right and mp[arr[i+right*m]] > cc[arr[i+right*m]]:
#                         mp[arr[i+left*m]] -= 1
#                         left += 1
#                     right += 1
#                     if right - left == n:
#                         res += [i+left*m]
#                 else:
#                     mp = Counter()
#                     left = right + 1
#                     right += 1
            
#         return res
                    
            
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        # initialize d, l, ans
        l = len(words[0])
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        i = 0
        ans = []

        # sliding window(s)
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0

        return ans 
