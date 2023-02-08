class Allocator:

    def __init__(self, n: int):
        self.state = [0]*n 


    def allocate(self, size: int, mID: int) -> int:
        n = len(self.state)
        cnt, start = 0, -1
        for i in range(n):
            if cnt == 0 and self.state[i] == 0:
                start = i 
            if self.state[i] == 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= size:
                for j in range(start, start+size):
                    self.state[j] = mID
                # print(self.state)
                return start
        # print(self.state)
        return -1


    def free(self, mID: int) -> int:
        n = len(self.state)
        cnt = 0
        for i in range(n):
            if self.state[i] == mID:
                self.state[i] = 0
                cnt += 1
        # print(self.state)
        return cnt



# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

class Allocator:

    def __init__(self, n: int):
        self.capacity = [n-i for i in range(n)]


    def allocate(self, size: int, mID: int) -> int:
        n = len(self.capacity)
        for i in range(n):
            if self.capacity[i] >= size:
                for j in range(size):
                    self.capacity[i+j] = -mID
                return i  
        return -1


    def free(self, mID: int) -> int:
        n = len(self.capacity)
        cnt = 0
        room = 0
        for i in range(n)[::-1]:
            if self.capacity[i] == -mID:
                cnt += 1
                room += 1
                self.capacity[i] = room
            else:
                if self.capacity[i] >= 0:
                    self.capacity[i] = room+1
                room = max(self.capacity[i],0)
        # print( "freed ", mID, cnt, self.capacity)
        return cnt



# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)