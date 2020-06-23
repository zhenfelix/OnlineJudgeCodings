class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        closest = []
        locs = collections.defaultdict(collections.deque)
        for i, lake in enumerate(rains):
            locs[lake].append(i)
        ret = []
        for i, lake in enumerate(rains):
            if closest and closest[0] == i:
                return []
            if not lake:
                if not closest:
                    ret.append(1) 
                    continue
                nxt = heapq.heappop(closest)
                ret.append(rains[nxt])
            else:
                l = locs[lake]
                l.popleft()
                if l:
                    nxt = l[0]
                    heapq.heappush(closest, nxt)
                ret.append(-1)
        return ret


# class Node:

#     def __init__(self, v, h):
#         self.val = v 
#         self.nxt = [None]*h

# class Skiplist:

#     def __init__(self):
#         self.head = Node(-float('inf'),1)
#         self.tail = Node(float('inf'),1)
#         self.H = 1
#         self.head.nxt[-1] = self.tail

#     def coinflip(self):
#         h = 1
#         while random.uniform(0,1) < 0.5:
#             h += 1
#         return h 
        

#     def search(self, target: int) -> bool:
#         cur = self.head
#         for i in range(self.H)[::-1]:
#             while cur.nxt[i].val <= target:
#                 cur = cur.nxt[i]
#         cur = cur.nxt[i]
#         return cur.val
        

#     def add(self, num: int) -> None:
#         h = self.coinflip()
#         self.H = max(self.H, h)
#         while len(self.head.nxt) < self.H:
#             self.head.nxt.append(self.tail)
#         cur = self.head
#         x = Node(num,h)
#         for i in range(self.H)[::-1]:
#             while cur.nxt[i].val <= num:
#                 cur = cur.nxt[i]
#             if i < h:
#                 x.nxt[i] = cur.nxt[i]
#                 cur.nxt[i] = x

#     def erase(self, num: int) -> bool:
#         x = self.head
#         flag = False
#         for i in range(self.H)[::-1]:
#             while x.nxt[i].val < num:
#                 x = x.nxt[i]
#             if x.nxt[i].val == num:
#                 flag = True
#                 x.nxt[i] = x.nxt[i].nxt[i]
#         return flag 



# class Solution:
#     def avoidFlood(self, rains: List[int]) -> List[int]:
#         seen = {}
#         st = Skiplist()
#         ans = [-1]*len(rains)
#         for i, r in enumerate(rains):
#             if r > 0:
#                 if r in seen:
#                     idx = st.search(seen[r])
#                     if idx == float('inf'):
#                         return []
#                     ans[idx] = r
#                     st.erase(idx)
#                 seen[r] = i
#             else:
#                 st.add(i)
#         while True:
#             idx = st.search(-float('inf'))
#             if idx == float('inf'):
#                 break
#             ans[idx] = 1
#             st.erase(idx)
#         return ans