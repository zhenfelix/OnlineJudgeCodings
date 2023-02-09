class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = []
        available = list(range(k))
        cnt = [0]*k
        for i, t in enumerate(arrival):

            while busy and busy[0][0] <= t:
                _, j = heappop(busy)
                if i > j:
                    j += ((i-j-1)//k+1)*k
                heappush(available,j)
            if available:
                j = heappop(available)
                j %= k
                cnt[j] += 1
                heappush(busy, (t+load[i],j))
                # print(i,t,j)
        mx = max(cnt)
        return [i for i in range(k) if cnt[i] == mx]


from heapq import *
from functools import total_ordering


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        heap_free = list(range(k))
        heap_busy = []
        count = [0] * k
        for i, (a, l) in enumerate(zip(arrival, load)):
            while heap_busy and heap_busy[0][0] <= a:
                _, server = heappop(heap_busy)
                # Rename this server to s2, s2 == server + u * k, s2 >= i
                multiples = i//k
                server = server%k+multiples*k
                if server < i:
                    server += k
                heappush(heap_free, server)
            if not heap_free:
                continue
            server = heappop(heap_free)
            count[server % k] += 1
            heappush(heap_busy, (a + l, server))
        mc = max(count)
        return [i for i in range(k) if count[i] == mc]




# 作者：ling-jian-2012
# 链接：https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests/solution/fei-chang-jian-dan-de-onlognsuan-fa-hao-shi-jin-48/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        left, right, servers = [], [], [(0,i) for i in range(k)]
        heapq.heapify(servers)
        cc = [0]*k
        for rank, t in enumerate(arrival):
            i = rank%k
            # print(i,t,servers,left,right)
            if i == 0:
                left, right = right, left
            if right and right[0] < i:
                heapq.heappush(left, heapq.heapop(right))
            while servers and t >= servers[0][0]:
                end, idx = heapq.heappop(servers)
                if idx >= i:
                    heapq.heappush(right, idx)
                else:
                    heapq.heappush(left, idx)
            if right:
                idx = heapq.heappop(right)
                heapq.heappush(servers, (t+load[rank], idx))
                cc[idx] += 1
            elif left:
                idx = heapq.heappop(left)
                heapq.heappush(servers, (t+load[rank], idx))
                cc[idx] += 1
        mx = max(cc)
        # print(cc)
        return [i for i in range(k) if cc[i] == mx]


# import heapq
# import bisect
# import re

# class TreeSet(object):
#     """
#     Binary-tree set like java Treeset.
#     Duplicate elements will not be added.
#     When added new element, TreeSet will be sorted automatically.
#     """
#     def __init__(self, elements):
#         self._treeset = []
#         self.addAll(elements)

#     def addAll(self, elements):
#         for element in elements:
#             if element in self: continue
#             self.add(element)

#     def add(self, element):
#         if element not in self:
#             bisect.insort(self._treeset, element)

#     def ceiling_index(self, e, exclusive=False):
#         index = bisect.bisect_right(self._treeset, e)
#         if exclusive:
#             return index
#         if index > 0 and self[index - 1] == e:
#             return index - 1
#         return index

#     def floor_index(self, e, exclusive=False):
#         index = bisect.bisect_left(self._treeset, e)
#         if exclusive:
#             return index - 1
#         if index < len(self) and self[index] == e:
#             return index
#         return index - 1

#     def ceiling(self, e, exclusive=False):
#         index = self.ceiling_index(e, exclusive)
#         if 0 <= index < len(self):
#             return self[index]
#         return None

#     def floor(self, e, exclusive=False):
#         index = self.floor_index(e, exclusive)
#         if 0 <= index < len(self):
#             return self[index]
#         return None

#     def __getitem__(self, num):
#         return self._treeset[num]

#     def __len__(self):
#         return len(self._treeset)

#     def clear(self):
#         """
#         Delete all elements in TreeSet.
#         """
#         self._treeset = []

#     def clone(self):
#         """
#         Return shallow copy of self.
#         """
#         return TreeSet(self._treeset)

#     def remove(self, element):
#         """
#         Remove element if element in TreeSet.
#         """
#         try:
#             self._treeset.remove(element)
#         except ValueError:
#             return False
#         return True

#     def __iter__(self):
#         """
#         Do ascending iteration for TreeSet
#         """
#         for element in self._treeset:
#             yield element

#     def pop(self, index):
#         return self._treeset.pop(index)

#     def __str__(self):
#         return str(self._treeset)

#     def __eq__(self, target):
#         if isinstance(target, TreeSet):
#             return self._treeset == target.treeset
#         elif isinstance(target, list):
#             return self._treeset == target

#     def __contains__(self, e):
#         """
#         Fast attribution judgment by bisect
#         """
#         try:
#             return e == self._treeset[bisect.bisect_left(self._treeset, e)]
#         except:
#             return False


# class Solution:
#     def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
#         count = [0 for _ in range(k)]
#         ts = TreeSet(list(range(k)))
#         h = []
#         for i, a in enumerate(arrival):
#             l = load[i]
#             while h and h[0][0] <= a:
#                 ts.add(h[0][1])
#                 heapq.heappop(h)
#             idx = i % k
#             t = ts.ceiling(idx)
#             if t is None:
#                 t = ts.ceiling(-1)
#             if t is not None:
#                 ts.remove(t)
#                 heapq.heappush(h, (a + l, t))
#                 count[t] += 1
#         m = max(count)
#         return [i for i, c in enumerate(count) if c == m]



from random import random
from math import log, ceil

class Node:
    __slots__ = ['value', 'next', 'width']
    def __init__(self, value, next, width):
        self.value, self.next, self.width = value, next, width

class End:
    'Sentinel object that always compares greater than another object'
    def __lt__(self, other):
        return False
    def __le__(self, other):
        return False
    def __gt__(self, other):
        return True
    def __ge__(self, other):
        return True

# tail = Node(End(), [], [])               # Singleton terminator node
tail = Node(float('inf'), [], [])               # Singleton terminator node


class Skiplist:
    'Sorted collection supporting O(lg n) insertion, removal, and lookup by rank.'

    def __init__(self, expected_size=50000):
        self.size = 0
        self.maxlevels = int(1 + log(expected_size, 2))
        self.head = Node(-float('inf'), [tail]*self.maxlevels, [1]*self.maxlevels)

    def __len__(self):
        return self.size

    def __getitem__(self, i):
        node = self.head
        i += 1
        for level in range(self.maxlevels)[::-1]:
            while node.width[level] <= i:
                i -= node.width[level]
                node = node.next[level]
        return node.value

    def search(self, value):
        # find first node on each level where node.next[levels].value > value
        step = 0
        node = self.head
        for level in range(self.maxlevels)[::-1]:
            while node.next[level].value <= value:
                step += node.width[level]
                node = node.next[level]
        # return step 
        return node.next[0].value

    def add(self, value):
        # find first node on each level where node.next[levels].value > value
        chain = [None] * self.maxlevels
        steps_at_level = [0] * self.maxlevels
        node = self.head
        for level in range(self.maxlevels)[::-1]:
            while node.next[level].value <= value:
                steps_at_level[level] += node.width[level]
                node = node.next[level]
            chain[level] = node

        # insert a link to the newnode at each level
        d = min(self.maxlevels, 1 - int(log(random(), 2.0)))
        newnode = Node(value, [None]*d, [None]*d)
        steps = 0
        for level in range(d):
            prevnode = chain[level]
            newnode.next[level] = prevnode.next[level]
            prevnode.next[level] = newnode
            newnode.width[level] = prevnode.width[level] - steps
            prevnode.width[level] = steps + 1
            steps += steps_at_level[level]
        for level in range(d, self.maxlevels):
            chain[level].width[level] += 1
        self.size += 1

    def erase(self, value):
        # find first node on each level where node.next[levels].value >= value
        chain = [None] * self.maxlevels
        node = self.head
        for level in range(self.maxlevels)[::-1]:
            while node.next[level].value < value:
                node = node.next[level]
            chain[level] = node
        if value != chain[0].next[0].value:
            # raise KeyError('Not Found')
            return False

        # remove one link at each level
        d = len(chain[0].next[0].next)
        for level in range(d):
            prevnode = chain[level]
            prevnode.width[level] += prevnode.next[level].width[level] - 1
            prevnode.next[level] = prevnode.next[level].next[level]
        for level in range(d, self.maxlevels):
            chain[level].width[level] -= 1
        self.size -= 1
        return True

    def __iter__(self):
        'Iterate over values in sorted order'
        node = self.head.next[0]
        while node is not tail:
            yield node.value
            node = node.next[0]




class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = [(0,i) for i in range(k)]
        cc = [0]*k
        sk = Skiplist()
        for i, t in enumerate(arrival):
            idx = i%k 
            while servers and servers[0][0] <= t:
                end, j = heapq.heappop(servers)
                sk.add(j)
            # print(i,t,[x for x in sk])
            j = sk.search(idx-1)
            # print(j)
            if j == float('inf'):
                j = sk.search(-1)
            if j == float('inf'):
                continue
            sk.erase(j)
            cc[j] += 1
            heapq.heappush(servers, (t+load[i], j))
            # print(i,t,servers,j)

        mx = max(cc)
        # print(cc)
        return [i for i in range(k) if cc[i] == mx]