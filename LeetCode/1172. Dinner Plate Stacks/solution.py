# import heapq

# class DinnerPlates:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.st = []
#         self.front = []
#         self.back = []

#     def push(self, val: int) -> None:
#         if len(self.front) == 0:
#             heapq.heappush(self.front, len(self.st))
#             self.st.append([])
#         if len(self.st[self.front[0]]) == 0:
#             heapq.heappush(self.back, -self.front[0])
#         self.st[self.front[0]].append(val)
#         if len(self.st[self.front[0]]) == self.capacity:
#             heapq.heappop(self.front)

#     def pop(self) -> int:
#         if len(self.back) == 0:
#             return -1
#         if len(self.st[-self.back[0]]) == self.capacity:
#             heapq.heappush(self.front, -self.back[0])
#         res = self.st[-self.back[0]].pop()
#         if len(self.st[-self.back[0]]) == 0:
#             heapq.heappop(self.back)
#         return res
        

#     def popAtStack(self, index: int) -> int:
#         if index >= len(self.st) or len(self.st[index]) == 0:
#             return -1
#         if len(self.st[index]) == self.capacity:
#             heapq.heappush(self.front, index)
#         res = self.st[index].pop()
#         if len(self.st[index]) == 0:
#             heapq.heappop(self.back)
#         return res


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.st = []
        self.capacity = capacity
        self.first = 0
        self.last = -1
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.first < len(self.st) and len(self.st[self.first]) == self.capacity:
            self.first += 1
        if self.first == len(self.st):
            self.st.append([])
        if len(self.st[self.first]) == 0:
            self.last = max(self.last, self.first)
        self.st[self.first].append(val)
        
        return

    def pop(self):
        """
        :rtype: int
        """
        while self.last >= 0 and len(self.st[self.last]) == 0:
            self.last -= 1
        if self.last == -1:
            return -1
        if len(self.st[self.last]) == self.capacity:
            self.first = min(self.first, self.last)
        res = self.st[self.last].pop()
        
        return res
        
   
    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= len(self.st) or len(self.st[index]) == 0:
            return -1
        if len(self.st[index]) == self.capacity:
            self.first = min(self.first, index)
        res = self.st[index].pop()
        return res