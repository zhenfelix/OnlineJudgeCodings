# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)


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

tail = Node(End(), [], [])               # Singleton terminator node
# tail = Node(float('inf'), [], [])               # Singleton terminator node


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
            while node.next[level].value < value:
            # while node.next[level].value <= value:
                step += node.width[level]
                node = node.next[level]
        return step 
        # return node.value == value

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
    def minInteger(self, num: str, k: int) -> str:
        digits = defaultdict(deque)
        arr = Skiplist(30000)
        for i, c in enumerate(num):
            digits[c].append(i)
            arr.add(i)
        ret = ''
        for _ in range(len(num)):
            for c in "0123456789":
                if digits[c]:
                    idx = digits[c][0]
                    pre_cnt = arr.search(idx)
                    if pre_cnt <= k:
                        k -= pre_cnt
                        ret += c
                        arr.erase(digits[c].popleft())
                        break
        return ret