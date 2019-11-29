# class Skiplist:

#     def __init__(self):
#         # random.seed(a=1023)
#         self.height = 0
#         self.head = Node()
#         self.head.nxt[-1] = self.head.pre[-1] = self.head

#     def search(self, target: int) -> bool:
#         # self.show()
#         cur = self.search_(target)
#         if cur != self.head and cur.val == target:
#             return True
#         return False

#     def search_(self, target):
#         idx = self.height
#         cur = self.head
#         while idx >= 0:
#             while cur.nxt[idx] != self.head and cur.nxt[idx].val <= target:
#                 cur = cur.nxt[idx]
#             idx -= 1
#         return cur

#     def coinFlip(self):
#         prob = 0.5
#         return random.uniform(0, 1) < prob

#     # def show(self):
#     #     head = self.head
#     #     height = len(head.nxt)
#     #     for idx in range(height):
#     #         cur = head
#     #         level = [cur.val]
#     #         while cur.nxt[idx] != self.head:
#     #             tmp_ = cur.nxt[0]
#     #             while tmp_ != cur.nxt[idx]:
#     #                 level.append('#')
#     #                 tmp_ = tmp_.nxt[0]
#     #             level.append(cur.nxt[idx].val)
#     #             cur = cur.nxt[idx]
#     #         print('level', idx, level)
#     #     print('\n')
#     #     return

#     def add(self, num: int) -> None:
#         # self.show()
#         cur = self.search_(num)
#         node = Node(num)
#         self.insertAfter(cur, node)
#         while self.coinFlip():
#             node.nxt.append(None)
#             node.pre.append(None)
#             while cur != self.head and len(node.nxt) > len(cur.nxt):
#                 cur = cur.pre[-1]
#             if cur == self.head and len(node.nxt) > len(cur.nxt):
#                 cur.nxt.append(self.head)
#                 cur.pre.append(self.head)
#             self.insertAfter(cur, node)
#         self.height = len(self.head.nxt) - 1
#         return

#     def insertAfter(self, cur, node):
#         idx = len(node.nxt) - 1
#         pre, nxt = cur, cur.nxt[idx]
#         node.nxt[idx], node.pre[idx] = nxt, pre
#         nxt.pre[idx], pre.nxt[idx] = node, node
#         return

#     def erase(self, num: int) -> bool:
#         # self.show()
#         cur = self.search_(num)
#         if cur != self.head and cur.val == num:
#             self.delete(cur)
#             return True
#         return False

#     def delete(self, node):
#         h = len(node.nxt)
#         for idx in range(h):
#             pre, nxt = node.pre[idx], node.nxt[idx]
#             pre.nxt[idx], nxt.pre[idx] = nxt, pre
#         return
    
# class Node:
#     def __init__(self, val=None):
#         self.val = val
#         self.pre = [None]
#         self.nxt = [None]


# # Your Skiplist object will be instantiated and called as such:
# # obj = Skiplist()
# # param_1 = obj.search(target)
# # obj.add(num)
# # param_3 = obj.erase(num)


class Node:
    __slots__ = 'val', 'levels'
    def __init__(self, val, levels):
        self.val = val
        self.levels = [None] * levels

class Skiplist(object):
    def __init__(self):
        self.head = Node(-1, 16) 
    
    def _iter(self, num):
        cur = self.head
        for level in range(15, -1, -1):
            while True:
                future = cur.levels[level]
                if future and future.val < num:
                    cur = future
                else:
                    break
            yield cur, level

    def search(self, target):
        for prev, level in self._iter(target):
            pass
        cur = prev.levels[0]
        return cur and cur.val == target

    def add(self, num):
        nodelvls = min(16, 1 + int(math.log2(1.0 / random.random())))
        node = Node(num, nodelvls)
        
        for cur, level in self._iter(num):
            if level < nodelvls:
                future = cur.levels[level]
                cur.levels[level] = node
                node.levels[level] = future

    def erase(self, num):
        ans = False
        for cur, level in self._iter(num):
            future = cur.levels[level]
            if future and future.val == num:
                ans = True
                cur.levels[level] = future.levels[level]
        return ans