# 手写双向链表
class Node:
    __slots__ = ('prev', 'next', 'ch')

    def __init__(self, ch=''):
        self.prev = None
        self.next = None
        self.ch = ch

    # 在 self 后插入 node，并返回该 node
    def insert(self, node: 'Node') -> 'Node':
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    # 从链表中移除 self
    def remove(self) -> None:
        self.prev.next = self.next
        self.next.prev = self.prev

class TextEditor:
    def __init__(self):
        self.root = self.cur = Node()  # 哨兵节点
        self.root.prev = self.root
        self.root.next = self.root  # 初始化双向链表，下面判断节点的 next 若为 self.root，则表示 next 为空

    def addText(self, text: str) -> None:
        for ch in text:
            self.cur = self.cur.insert(Node(ch))

    def deleteText(self, k: int) -> int:
        k0 = k
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            self.cur.next.remove()
            k -= 1
        return k0 - k

    def text(self) -> str:
        s = []
        k, cur = 10, self.cur
        while k and cur != self.root:
            s.append(cur.ch)
            cur = cur.prev
            k -= 1
        return ''.join(reversed(s))

    def cursorLeft(self, k: int) -> str:
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.cur.next != self.root:
            self.cur = self.cur.next
            k -= 1
        return self.text()


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/design-a-text-editor/solution/lian-biao-mo-ni-pythonjavacgo-by-endless-egw4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class TextEditor:
    def __init__(self):
        self.left, self.right = [], []

    def addText(self, text: str) -> None:
        self.left.extend(list(text))

    def deleteText(self, k: int) -> int:
        k0 = k
        while k and self.left:
            self.left.pop()
            k -= 1
        return k0 - k

    def text(self) -> str:
        return ''.join(self.left[-10:])

    def cursorLeft(self, k: int) -> str:
        while k and self.left:
            self.right.append(self.left.pop())
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.right:
            self.left.append(self.right.pop())
            k -= 1
        return self.text()


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/design-a-text-editor/solution/lian-biao-mo-ni-pythonjavacgo-by-endless-egw4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。