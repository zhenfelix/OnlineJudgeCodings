class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dummy = Freq(0)
        self.f2freq = {}
        self.k2node = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.k2node:
            return -1
        cur = self.k2node[key]
        backbone = self.f2freq[cur.freq]
        cur.freq += 1
        backbone = self.removeNode(cur, backbone)
        self.insertNode(cur, backbone)
        return cur.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.k2node:
            self.k2node[key].value = value
            self.get(key)
            return
        if self.capacity == 0:
            if not self.dummy.next:
                return
            remove_key = self.dummy.next.tail.key
            self.removeNode(self.dummy.next.tail, self.dummy.next)
            # print(key, value, remove_key, self.k2node)
            del self.k2node[remove_key]
        else:
            self.capacity -= 1
        cur = Node(key, value)
        cur.freq = 1
        self.k2node[key] = cur
        self.insertNode(cur, self.dummy)
        return

    def removeNode(self, cur, backbone):
        if not cur.pre and not cur.next:
            pre_backbone = backbone.pre
            pre_backbone.next = backbone.next
            if backbone.next:
                backbone.next.pre = pre_backbone
            del self.f2freq[backbone.freq]
            return pre_backbone
        if not cur.pre:
            backbone.head = cur.next
            cur.next.pre = None
            cur.next = None
        elif not cur.next:
            backbone.tail = cur.pre
            cur.pre.next = None
            cur.pre = None
        else:
            cur.pre.next, cur.next.pre = cur.next, cur.pre
            cur.pre, cur.next = None, None
        return backbone

    def insertNode(self, cur, backbone):
        f = cur.freq
        if f not in self.f2freq:
            new_backbone = Freq(f)
            self.f2freq[f] = new_backbone
            new_backbone.head, new_backbone.tail = cur, cur
            new_backbone.pre, new_backbone.next = backbone, backbone.next
            if backbone.next:
                backbone.next.pre = new_backbone
            backbone.next = new_backbone

        else:
            new_backbone = self.f2freq[f]
            nxt = new_backbone.head
            new_backbone.head, cur.next, nxt.pre = cur, nxt, cur
        return


class Freq:
    """docstring for Freq"""

    def __init__(self, freq=0):
        self.freq = freq
        self.next = None
        self.pre = None
        self.head = None
        self.tail = None


class Node:
    """docstring for Node"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = -1
        self.pre = None
        self.next = None