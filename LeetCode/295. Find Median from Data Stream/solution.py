# class MyHeap():
#     def __init__(self, key = lambda x: x):
#         self.arr = []
#         self.func = key
    
#     def push(self, a):
#         self.arr.append(a)
#         self._go_up(len(self.arr)-1)
        
#     def pop(self):
#         front = self.arr[0]
#         self.arr[0] = self.arr[-1]
#         self.arr.pop()
#         self._go_down(0)
#         return front
    
#     def peek(self):
#         return self.arr[0]
        
#     def _go_up(self, idx):
#         func = self.func
#         arr = self.arr
#         parent = (idx-1)//2
#         if idx == 0 or func(arr[parent]) <= func(arr[idx]):
#             return
#         self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
#         self._go_up(parent)
#         return
    
#     def _go_down(self, idx):
#         func = self.func
#         arr = self.arr
#         left, right = idx*2+1, idx*2+2
#         n = len(arr)
#         if left >= n:
#             return
#         if right < n and func(arr[right]) < func(arr[left]):
#             left, right = right, left
#         if func(arr[idx]) > func(arr[left]):
#             self.arr[idx], self.arr[left] = self.arr[left], self.arr[idx]
#             self._go_down(left)
#         return


class MyHeap():
    def __init__(self, key = lambda x: x):
        self.arr = []
        self.func = key
    
    def push(self, a):
        self.arr.append(a)
        self._go_up(len(self.arr)-1)
        
    def pop(self):
        front = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self._go_down(0)
        return front
    
    def pushpop(self, a):
        func = self.func
        arr = self.arr
        if len(arr) == 0 or func(a) <= func(arr[0]):
            return a
        self.arr.append(a)
        return self.pop()
        
    
    def peek(self):
        return self.arr[0]
        
    # def _go_up(self, idx):
    #     func = self.func
    #     arr = self.arr
    #     while idx > 0:
    #         parent = (idx-1)>>1
    #         if func(arr[parent]) <= func(arr[idx]):
    #             break
    #         self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
    #         idx = parent
    #     return

    def _go_up(self, idx):
        func = self.func
        arr = self.arr
        pre = arr[idx]
        while idx > 0:
            parent = (idx-1)>>1
            # print('pushed: ', pre, 'parent: ', parent, 'idx: ', idx)
            # print(self.arr)
            if func(arr[parent]) <= func(pre):
                break
            # print('pushed: ', pre, 'parent: ', parent, 'idx: ', idx)
            # print(self.arr)
            self.arr[idx] = self.arr[parent] 
            idx = parent
        self.arr[idx] = pre
        return
    
    def _go_down(self, idx):
        func = self.func
        arr = self.arr
        left, right = idx*2+1, idx*2+2
        n = len(arr)
        pre = arr[idx]
        while left < n:
            if right < n and func(arr[right]) < func(arr[left]):
                left, right = right, left
            if func(pre) <= func(arr[left]):
                break
            self.arr[idx] = self.arr[left]
            idx = left
            left, right = idx*2+1, idx*2+2
        self.arr[idx] = pre
        return
            
        
    
    


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = MyHeap()
        self.maxHeap = MyHeap(key=lambda x: -x)
        self.size = 0

    def addNum(self, num: int) -> None:
        size = self.size
        if size%2 == 0:
            # if size > 1 and self.maxHeap.peek() > num:
            num = self.maxHeap.pushpop(num)
            self.minHeap.push(num)
        else:
            # if size > 0 and self.minHeap.peek() < num:
            num = self.minHeap.pushpop(num)
            self.maxHeap.push(num)
            
        self.size += 1

    def findMedian(self) -> float:
        size = self.size
        # print("minHeap: ", self.minHeap.arr)
        # print("maxHeap: ", self.maxHeap.arr)
        if size%2 == 1:
            return self.minHeap.peek()
        else:
            return (self.minHeap.peek()+self.maxHeap.peek())/2

        
        
# import heapq

# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.lows = []
#         self.highs = []

#     def addNum(self, num: int) -> None:
#         if (len(self.lows) < len(self.highs)):
#             num = heapq.heappushpop(self.highs, num)
#             heapq.heappush(self.lows, -num)
#         else:
#             num = heapq.heappushpop(self.lows, -num)
#             heapq.heappush(self.highs, -num)

#     def findMedian(self) -> float:
#         if (len(self.lows) == len(self.highs)):
#             return (self.highs[0] - self.lows[0]) / 2
#         else:
#             return self.highs[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()