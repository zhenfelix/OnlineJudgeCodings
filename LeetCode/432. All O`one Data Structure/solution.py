class Node:

    def __init__(self, key = "", freq = 0):
        self.keys = set([key])
        self.freq = freq
        self.next = None
        self.pre = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k2node = {}
        self.dummy = Node()
        self.dummy.next, self.dummy.pre = self.dummy, self.dummy

    def _remove(self,cur,key):
        f = cur.freq
        cur.keys.remove(key)
        del self.k2node[key]
        left, right = cur.pre, cur.next
        if not cur.keys:
            pre = cur.pre
            cur.pre.next, cur.next.pre = cur.next, cur.pre
            cur.pre, cur.next = None, None
        return left, right, f
            

    def _insert(self,left,right,key,f):
        if f == 0:
            return
        if f == left.freq:
            left.keys.add(key)
            self.k2node[key] = left
        elif f == right.freq:
            right.keys.add(key)
            self.k2node[key] = right
        else:
            mid = Node(key,f)
            mid.next, mid.pre = right, left
            mid.next.pre, mid.pre.next = mid, mid
            self.k2node[key] = mid
        return



    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.k2node:
            cur = self.k2node[key]
            left, right, f = self._remove(cur,key)
            if cur.pre or cur.next:
                left = cur
        else:
            left, right, f = self.dummy, self.dummy.next, 0
        self._insert(left,right,key,f+1)
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.k2node:
            return
        cur = self.k2node[key]
        left, right, f = self._remove(cur,key)
        if cur.pre or cur.next:
            right = cur
        self._insert(left,right,key,f-1)

        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.dummy.pre.keys))
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.dummy.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()