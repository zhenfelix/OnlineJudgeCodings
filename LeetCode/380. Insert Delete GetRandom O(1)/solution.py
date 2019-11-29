# class RandomizedSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head = Node()
#         self.idx2node = {}
#         self.val2node = {}
#         self.sz = 0

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val in self.val2node:
#             return False
#         self.sz += 1
#         node = Node(self.sz, val)
#         pre, nxt = self.head.pre, self.head
#         self.insert_(pre,nxt,node)
#         self.idx2node[self.sz] = node
#         self.val2node[val] = node 
#         # print("insert",self.idx2node, self.val2node)
#         return True 

#     def insert_(self, pre, nxt, node):
#         pre.nxt, nxt.pre = node, node
#         node.pre, node.nxt = pre, nxt
#         return


#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val not in self.val2node:
#             return False
#         node = self.val2node[val]
#         pre, nxt = node.pre, node.nxt
#         idx = node.idx
#         del self.val2node[val]
#         self.idx2node[idx] = self.idx2node[self.sz]
#         self.remove_(self.idx2node[idx])
#         if idx != self.sz:
#             self.insert_(pre,nxt,self.idx2node[idx])
#             self.idx2node[idx].idx = idx
#         del self.idx2node[self.sz]
#         self.sz -= 1
#         # print("remove",self.idx2node, self.val2node)
#         return True

#     def remove_(self, node):
#         pre, nxt = node.pre, node.nxt
#         pre.nxt, nxt.pre = nxt, pre
#         return
        

#     def getRandom(self) -> int:
#         """.
#         Get a random element from the set.
#         """
#         idx = random.randint(1,self.sz)
#         # print("random",self.idx2node, self.val2node)
#         return self.idx2node[idx].val
        
# class Node:

#     def __init__(self, idx = 0, val = None):
#         self.nxt = self.pre = self
#         self.idx = idx
#         self.val = val

# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mp:
            return False
        self.mp[val] = len(self.st)
        self.st.append(val)
        return True 


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.mp:
            return False
        idx = self.mp[val]
        self.st[-1], self.st[idx] = self.st[idx], self.st[-1]
        self.mp[self.st[idx]] = idx
        del self.mp[val]
        self.st.pop()
        return True

    def getRandom(self) -> int:
        """.
        Get a random element from the set.
        """
        idx = random.randint(0,len(self.st)-1)
        return self.st[idx]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()