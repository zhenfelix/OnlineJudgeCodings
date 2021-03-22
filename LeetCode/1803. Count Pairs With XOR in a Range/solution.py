# class Solution:
#     def countPairs(self, nums: List[int], low: int, high: int) -> int:
#         # maxn, maxk = 2*10**4+5, 16
#         maxn, maxk = len(nums)+5, 16
#         tree = [[0]*2 for _ in range(maxn*maxk)]
#         cnt = [0]*(maxn*maxk)
#         tot = 0

#         def insert(x):
#             nonlocal tot
#             cur = 0
#             # cnt[cur] += 1
#             for i in range(16)[::-1]:
#                 state = (x>>i)&1
#                 if tree[cur][state] == 0:
#                     tot += 1
#                     tree[cur][state] = tot
#                 cur = tree[cur][state]
#                 cnt[cur] += 1

#         def query(x, lo):
#             # cur_x, cur_lo = 0, 0
#             cur, res = 0, 0
#             # print(x,lo,cur)
#             for i in range(16)[::-1]:
#                 cur_x, cur_lo = (x>>i)&1, (lo>>i)&1
#                 state = cur_x ^ cur_lo
#                 if cur_lo == 0:
#                     res += cnt[tree[cur][1-state]]
#                     # state = 1-state
                    
#                 cur = tree[cur][state]
#                 # print(cur,cur_x,cur_lo,state)
#                 if cur == 0:
#                     return res
#             return res 

#         # for x in nums:
#         #     insert(x)
#         # print(tree[:30][:])
#         # print(cnt[:30])
#         ans = 0
#         for x in nums:
#             ans += query(x,low-1) - query(x,high)
#             insert(x)
#         return ans




# class Trie: 
#     def __init__(self): 
#         self.root = {}
        
#     def insert(self, val): 
#         node = self.root 
#         for i in reversed(range(15)):
#             bit = (val >> i) & 1
#             if bit not in node: 
#                 node[bit] = {"cnt": 1}
#             else: 
#                 node[bit]["cnt"] += 1
#             node = node[bit]
        
#     def count(self, val, high): 
#         ans = 0 
#         node = self.root
#         for i in reversed(range(15)):
#             if not node: break 
#             bit = (val >> i) & 1 
#             cmp = (high >> i) & 1
#             if cmp: 
#                 if node.get(bit, {}): 
#                     ans += node[bit]["cnt"]
#                 node = node.get(1^bit, {})
#             else: 
#                 node = node.get(bit, {})
#         return ans 
            
        
# class Solution:
#     def countPairs(self, nums: List[int], low: int, high: int) -> int:
#         trie = Trie()
        
#         ans = 0
#         for x in nums: 
#             ans += trie.count(x, high+1) - trie.count(x, low)
#             trie.insert(x)
#         return ans 

class Solution:
    def countPairs(self, A, low, high):
        def test(A, x):
            count = Counter(A)
            res = 0
            while x:
                if x & 1:
                    res += sum(count[a] * count[(x - 1) ^ a] for a in count)
                count = Counter({a >> 1: count[a] + count[a ^ 1] for a in count})
                x >>= 1
            return res // 2
        return test(A, high + 1) - test(A, low)