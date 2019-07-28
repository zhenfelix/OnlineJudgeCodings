# class Node:
    
#     def __init__(self, index, value, mp):
#         self.idx = index
#         self.val = value
#         self.pre = None
#         self.next = None
#         self.set(mp)
        
#     def set(self,mp):
#         mp[self.idx] = self

# class MyLinkedList:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.sz = 0
#         self.mp = {}
#         self.head = Node(-1,-1,self.mp)
#         self.tail = Node(-2,-2,self.mp)
#         self.head.next, self.tail.pre = self.tail, self.head

#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if index >= 0 and index < self.sz:
#             return self.mp[index].val
#         return -1

#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         newNode = Node(0,val,self.mp)
#         self._add(newNode,self.head.next)
#         self._change(0,newNode.next)
        
        

#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         newNode = Node(self.sz,val,self.mp)
#         self._add(newNode,self.tail)
#         self._change(self.sz,newNode.next)
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index == self.sz:
#             self.addAtTail(val)
#             return
#         if index < 0:
#             self.addAtHead(val)
#             return
#         if index > self.sz:
#             return
#         cur = self.mp[index]
#         newNode = Node(index,val,self.mp)
#         self._add(newNode,cur)
#         self._change(index,cur)

#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if index < 0 or index >= self.sz:
#             return
#         cur = self.mp[index]
#         self._remove(cur)
#         self._change(index+1,cur.next,False)
        
#     def _remove(self, cur):
#         pre, nxt = cur.pre, cur.next
#         pre.next, nxt.pre = nxt, pre
        
#     def _add(self, node, cur):
#         # print('node.val', node.val, 'self.mp', self.mp)
#         pre = cur.pre
#         pre.next, cur.pre, node.pre, node.next = node, node, pre, cur
        
#     def _change(self, idx, node, is_add=True):
#         for i in range(idx, self.sz):
#             if is_add:
#                 node.idx += 1
#                 node.set(self.mp)
#             else:
#                 node.idx -= 1
#                 node.set(self.mp)
#             node = node.next
#         if is_add:
#             self.sz += 1
#         else:
#             self.sz -= 1

# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
                
        print(f'get({index})', self)
        
        node = self.get_node(index)
        if node:
            return node.val
        else:
            return -1     

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        print(f"addAtHead({val})", self)
        
        self.add(ListNode(val), None, self.head)       
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        
        print(f"addAtTail({val})", self)        
        self.add(ListNode(val), self.tail, None)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        
        print(f"addAtIndex({index}, {val})", self)
        
        if index <= 0:
            return self.addAtHead(val)
        
        if not self.head:
            return None
        
        current = self.get_node(index-1)
        if current:        
            self.add(ListNode(val), current, current.next)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        print(f"deleteAtIndex({index})", self)        
        
        if index < 0:
            return
        
        if not self.head:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.get_node(index - 1)
        
        if current.next:
            current.next = current.next.next
            if not current.next:
                self.tail = current
    
    def add(self, current, prev, _next):
        if not current:
            return
        
        if not prev:
            self.head = current
        else:        
            prev.next = current
            
        if not _next:
            self.tail = current
        else:
            current.next = _next   
    
    def get_node(self, index):        
        
        if index < 0 or not self.head:
            return None
        
        current = self.head
        for i in range(index):
            current = current.next
            if not current:
                return None
        
        return current 
    
    def __repr__(self):
        current = self.head
        s = ""
        visited = set()
        while current and current not in visited:
            s += f'{current.val}->'
            visited.add(current)
            current = current.next
        
        if current:
            s += f'{current.val}->'
        
        return s

def sink(*args, **kwargs):
    pass

print = sink
    
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)