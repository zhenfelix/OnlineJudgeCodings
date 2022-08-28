class MyCircularDeque:

    def __init__(self, n: int):
        self.sz = 0
        self.n = n 
        self.arr = [-1]*n 
        self.left, self.right = 0, n-1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.left = (self.left-1+self.n)%self.n 
        self.arr[self.left] = value
        self.sz += 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.right = (self.right+1)%self.n 
        self.arr[self.right] = value
        self.sz += 1
        return True 


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.left = (self.left+1)%self.n 
        self.sz -= 1
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.right = (self.right-1+self.n)%self.n
        self.sz -= 1
        return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.left]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.right]


    def isEmpty(self) -> bool:
        return self.sz == 0


    def isFull(self) -> bool:
        return self.sz == self.n 



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()






class Node:
    __slots__ = 'prev', 'next', 'val'

    def __init__(self, val):
        self.prev = self.next = None
        self.val = val


class MyCircularDeque:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


作者：LeetCode-Solution
链接：https://leetcode.cn/problems/design-circular-deque/solution/she-ji-xun-huan-shuang-duan-dui-lie-by-l-97v0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。