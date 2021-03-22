class Node:
    def __init__(self, val=0, key=None, prev=None, nxt=None):
        self.expire = val
        self.key = key
        self.prev = prev
        self.next = nxt

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
    
    # 新建一个节点，塞到链表最后面，添加到哈希表里
    def generate(self, tokenId: str, currentTime: int) -> None:
        node = Node(currentTime + self.ttl, tokenId)
        self.map[tokenId] = node

        #塞到最后
        last = self.tail.prev
        last.next = node
        node.prev = last
        self.tail.prev = node
        node.next = self.tail

    # 如果这个节点存在且没有过期，那么把这个节点找出来，更新过期时间，塞到最后
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.map and self.map[tokenId].expire > currentTime:

            #从原来的地方取出来
            node = self.map[tokenId]
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
            #更新过期时间
            node.expire = currentTime + self.ttl
            #塞到最后
            last = self.tail.prev
            last.next = node
            node.prev = last
            self.tail.prev = node
            node.next = self.tail           
        
    # 在双向链表里把所有过期的节点删了，在哈希表里也删掉，返回长度
    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.head.next.expire != -1 and self.head.next.expire <= currentTime:
            node = self.head.next
            self.map.pop(node.key)
            self.head.next = node.next
            node.next.prev = self.head
        return len(self.map)


# # 作者：ddoudle
# # 链接：https://leetcode-cn.com/problems/design-authentication-manager/solution/jun-tan-o1-shuang-xiang-lian-biao-ha-xi-c4igt/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# class AuthenticationManager:

#     def __init__(self, timeToLive: int):
#         self.timeout = timeToLive
#         self.expire = {}

#     def generate(self, tokenId: str, currentTime: int) -> None:
#         self.expire[tokenId] = currentTime


#     def renew(self, tokenId: str, currentTime: int) -> None:
#         if tokenId in self.expire and currentTime - self.expire[tokenId] < self.timeout:
#             self.expire[tokenId] = currentTime


#     def countUnexpiredTokens(self, currentTime: int) -> int:
#         cnt = 0
#         for tokenId, t in self.expire.items():
#             if currentTime - t < self.timeout:
#                 cnt += 1
#         return cnt

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeout = timeToLive
        self.expire = {}
        self.q = deque()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expire[tokenId] = currentTime + self.timeout
        self.q.append((currentTime+self.timeout, tokenId))


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.expire and currentTime < self.expire[tokenId]:
            self.expire[tokenId] = currentTime + self.timeout
            self.q.append((currentTime+self.timeout, tokenId))


    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.q and self.q[0][0] <= currentTime:
            t, tokenId = self.q.popleft()
            if self.expire[tokenId] == t:
                self.expire.pop(tokenId)
        return len(self.expire)