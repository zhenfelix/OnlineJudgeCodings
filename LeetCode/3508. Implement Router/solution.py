class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_set = set()
        self.dest_q = deque()  # destination 队列
        self.dest_to_pairs = defaultdict(deque)  # destination -> [(timestamp, source)]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        self.packet_set.add(packet)
        if len(self.dest_q) == self.memory_limit:  # 太多了
            self.forwardPacket()
        self.dest_q.append(destination)  # 入队
        self.dest_to_pairs[destination].append((timestamp, source))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.dest_q:
            return []
        dest = self.dest_q.popleft()  # 出队
        timestamp, source = self.dest_to_pairs[dest].popleft()
        self.packet_set.remove((source, dest, timestamp))
        return [source, dest, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        pairs = self.dest_to_pairs[destination]
        left = bisect_left(pairs, startTime, key=lambda p: p[0])  # deque 访问不是 O(1) 的，可以看另一份代码
        right = bisect_right(pairs, endTime, key=lambda p: p[0])
        return right - left

作者：灵茶山艾府
链接：https://leetcode.cn/problems/implement-router/solutions/3641772/mo-ni-ha-xi-biao-dui-lie-er-fen-cha-zhao-y7l7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_set = set()
        self.dest_q = deque()  # destination 队列
        self.dest_to_pairs = defaultdict(lambda: ([], 0))  # destination -> ([(timestamp, source)], head_index)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        self.packet_set.add(packet)
        if len(self.dest_q) == self.memory_limit:  # 太多了
            self.forwardPacket()
        self.dest_q.append(destination)  # 入队
        self.dest_to_pairs[destination][0].append((timestamp, source))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.dest_q:
            return []
        dest = self.dest_q.popleft()  # 出队
        pairs, head = self.dest_to_pairs[dest]
        timestamp, source = pairs[head]
        head += 1
        self.dest_to_pairs[dest] = (pairs, head)
        self.packet_set.remove((source, dest, timestamp))
        return [source, dest, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        pairs, head = self.dest_to_pairs[destination]
        left = bisect_left(pairs, startTime, head, key=lambda p: p[0])
        right = bisect_right(pairs, endTime, head, key=lambda p: p[0])
        return right - left

作者：灵茶山艾府
链接：https://leetcode.cn/problems/implement-router/solutions/3641772/mo-ni-ha-xi-biao-dui-lie-er-fen-cha-zhao-y7l7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。