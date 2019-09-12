# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         def isPanlindrome(a, b):
#             s = a + b
#             return s == s[::-1]
#         n = len(words)
#         res = []
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     continue
#                 if isPanlindrome(words[i], words[j]):
#                     res += [[i,j]]
#         return res


# class TrieNode():
#     def __init__(self):
#         self.children = {}
#         self.end = -1
        
# class Trie():
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, string, idx):
#         cur = self.root
#         for ch in string:
#             if ch not in cur.children:
#                 cur.children[ch] = TrieNode()
#             cur = cur.children[ch]
#         cur.end = idx
#         return
    
#     def search(self, string):
#         cur = self.root
#         for ch in string:
#             if ch not in cur.children:
#                 return -1
#             cur = cur.children[ch]
#         return cur.end
    
#     # def debug(self):
#     #     return self.root.children
            
    
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         res = []
#         T = Trie()
#         # Set = set()
#         for i, word in enumerate(words):
#             T.insert(word,i)
#         for i, word in enumerate(words):
#             n = len(word)
#             idx = T.search(word[::-1])
#             if idx not in [-1,i]:
#                 res.append([idx,i])
#             for k in range(1,n+1):
#                 # print('k=', k, word[k+1:], word[n-1:k:-1])
#                 if word[n-k:] != word[-1:-k-1:-1]:
#                     continue
#                 # print('search', word[k:-1:-1])
#                 idx = T.search(word[-k-1::-1])
#                 # print('1st',i,idx)
#                 if idx not in [-1,i] and (i,idx):
#                     # Set.add((i,idx))
#                     res.append([i,idx])
#             for k in range(1,n+1):
#                 if word[:k] != word[-n+k-1::-1]:
#                     continue
#                 idx = T.search(word[-1:-n+k-1:-1])
#                 if idx not in [-1,i] and (idx,i):
#                     # Set.add((idx,i))
#                     res.append([idx,i])
#         return res
     
    
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         res = []
#         mp = {}
#         # Set = set()
#         for i, word in enumerate(words):
#             mp[word] = i
#         for i, word in enumerate(words):
#             n = len(word)
#             if word[::-1] in mp and mp[word[::-1]] != i:
#                 res.append([mp[word[::-1]],i])
            
#             for k in range(1,n+1):
#                 if word[n-k:] != word[-1:-k-1:-1]:
#                     continue
#                 if word[-k-1::-1] in mp and mp[word[-k-1::-1]] != i:
#                     res.append([i,mp[word[-k-1::-1]]])
#             for k in range(1,n+1):
#                 if word[:k] != word[-n+k-1::-1]:
#                     continue
#                 if word[-1:-n+k-1:-1] in mp and mp[word[-1:-n+k-1:-1]] != i:
#                     res.append([mp[word[-1:-n+k-1:-1]],i])
#         return res
    
class TrieNode():
    def __init__(self):
        self.children = {}
        self.rev_idx = -1
        self.idx = -1
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, string, idx, flag = True):
        cur = self.root
        for ch in string:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        if flag:
            cur.idx = idx
        else:
            cur.rev_idx = idx
        return
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        T = Trie()
        
        def manacher(nums):
            A = '#'+'#'.join(nums)+'#'
            center, reach = 0, 0
            Z = [0]*len(A)
            for i in range(len(A)):
                if i < reach:
                    Z[i] = min(reach-i, Z[2*center-i])
                while i+Z[i]+1 < len(A) and i-Z[i]-1 >= 0 and A[i+Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] += 1
                if i+Z[i] > reach:
                    center, reach = i, i+Z[i]
            return Z
                
        for i, word in enumerate(words):
            T.insert(word,i)
            T.insert(word[::-1],i,False)
            
        for i, word in enumerate(words):
            n = len(word)
            if n == 0: continue
            Z_ = manacher(word)
            # print(Z_)
            left, right = [False]*n, [False]*n
            for c, z in enumerate(Z_):
                r = (c+z-1)//2
                l = (c-z)//2
                # print(l,r)
                if l <= r and l == 0:
                    left[r] = True
                if l <= r and r == n-1:
                    right[l] = True
            # print(left, right)
            cur = T.root
            ch = ''
            for j in range(n-1,-1,-1):
                idx = cur.idx
                if idx != -1 and left[j]:
                    res.append([idx,i])
                ch = word[j]
                if ch not in cur.children:
                    break
                cur = cur.children[ch]
                
            cur = T.root
            ch = ''
            for j in range(n):
                idx = cur.rev_idx
                if idx != -1 and right[j]:
                    res.append([i,idx])
                ch = word[j]
                if ch not in cur.children:
                    break
                cur = cur.children[ch]
                
            if cur.idx == i and cur.rev_idx not in [i,-1]:
                res.append([i,cur.rev_idx])
        return res