# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cp = capacity
#         self.sz = 0
#         self.head = -2
#         self.tail = -1
#         self.mp = {}
#         self.mp[self.head] = {'val':-2, 'pre':-3, 'next':self.tail}
#         self.mp[self.tail] = {'val':-1, 'pre':self.head, 'next':0}

#     def get(self, key: int) -> int:
#         if key not in self.mp:
#             return -1
      
#         self.mp[self.mp[key]['pre']]['next'] = self.mp[key]['next']
#         self.mp[self.mp[key]['next']]['pre'] = self.mp[key]['pre']

#         pre = self.mp[self.tail]['pre']
#         self.mp[pre]['next'] = key
#         self.mp[key]['pre'] = pre
#         self.mp[key]['next'] = self.tail
#         self.mp[self.tail]['pre'] = key
  
#         return self.mp[key]['val']

#     def put(self, key: int, value: int) -> None:
#         # print(key)
#         if key in self.mp:
#             self.mp[self.mp[key]['pre']]['next'] = self.mp[key]['next']
#             self.mp[self.mp[key]['next']]['pre'] = self.mp[key]['pre']
#             del self.mp[key]
#             self.sz -= 1
#         elif self.sz == self.cp:
#             nxt = self.mp[self.head]['next']
#             self.mp[self.head]['next'] = self.mp[nxt]['next']
#             self.mp[self.mp[nxt]['next']]['pre'] = self.head
#             del self.mp[nxt]
#             self.sz -= 1
            
        
#         pre = self.mp[self.tail]['pre']
#         self.mp[pre]['next'] = key
#         self.mp[key] = {'val':value, 'pre':pre, 'next':self.tail}
#         self.mp[self.tail]['pre'] = key

#         self.sz += 1


class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)