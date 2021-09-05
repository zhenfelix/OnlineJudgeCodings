class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        n = len(parent)
        self.state = [0]*n 
        self.child = defaultdict(list)
        for i in range(n):
            if parent[i] == -1:
                continue
            self.child[parent[i]].append(i)
        # print(self.child)


    def lock(self, num: int, user: int) -> bool:
        if self.state[num] > 0:
            return False
        self.state[num] = user
        return True


    def unlock(self, num: int, user: int) -> bool:
        if self.state[num] != user:
            return False
        self.state[num] = 0
        return True


    def upgrade(self, num: int, user: int) -> bool:
        
        p = num
        while p != -1:
            if self.state[p] > 0:
                return False
            p = self.parent[p]
        flag = False
        q = deque()
        q.append(num)
        while q:
            cur = q.popleft()
            if self.state[cur] > 0:
                flag = True
                break
            for nxt in self.child[cur]:
                q.append(nxt)
        if not flag:
            return False
        q = deque()
        q.append(num)
        while q:
            cur = q.popleft()
            if self.state[cur] > 0:
                self.state[cur] = 0
            for nxt in self.child[cur]:
                q.append(nxt)
        self.state[num] = user
        return True





# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)