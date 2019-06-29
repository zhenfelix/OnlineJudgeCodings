# https://codereview.stackexchange.com/questions/197040/min-max-heap-implementation-in-python

# import operator


# class Heap(object):
#     """"
#     Attributes:
#         heap: List representation of the heap
#         compare(p, c): comparator function, returns true if the relation between p and c is parent-chield
#     """
#     def __init__(self, heap=None, compare=operator.lt):
#         self.heap = [] if heap is None else heap
#         self.compare = compare

#     def __repr__(self):
#         return 'Heap({!r}, {!r})'.format(self.heap, self.compare)

#     def _inv_heapify(self, child_index):
#         """
#         Do heapifying starting from bottom till it reaches the root.
#         """
#         heap, compare = self.heap, self.compare
#         child = child_index
#         while child > 0:
#             parent = child // 2
#             if compare(heap[parent], heap[child]):
#                 return
#             heap[parent], heap[child] = heap[child], heap[parent]
#             child = parent

#     def _heapify(self, parent_index):
#         """
#         Do heepifying starting from the root.
#         """
#         heap, compare = self.heap, self.compare
#         length = len(heap)
#         if length == 1:
#             return
#         parent = parent_index
#         while 2 * parent < length:
#             child = 2 * parent
#             if child + 1 < length and compare(heap[child + 1], heap[child]):
#                 child += 1
#             if compare(heap[parent], heap[child]):
#                 return
#             heap[parent], heap[child] = heap[child], heap[parent]
#             parent = child

#     def del_min(self):
#         heap = self.heap
#         last_element = heap.pop()
#         if not heap:
#             return last_element
#         item = heap[0]
#         heap[0] = last_element
#         self._heapify(0)
#         return item

#     def min(self):
#         if not self.heap:
#             return None
#         return self.heap[0]

#     def add(self, element):
#         self.heap.append(element)
#         self._inv_heapify(len(self.heap) - 1)


# class minheap:
    
#     def __init__(self):
#         self.arr=[]
        
#     def push(self,a):
#         self.arr.append(a)
#         self.go_up()
#         return
        
#     def pop(self):
#         self.go_down()
#         return 
    
#     def top(self):
#         return self.arr[0]
    
#     def size(self):
#         return len(self.arr)
        
#     def go_up(self):
#         idx=len(self.arr)-1
#         while idx>0 and self.arr[idx]<self.arr[(idx-1)//2]:
#             self.arr[idx],self.arr[(idx-1)//2]=self.arr[(idx-1)//2],self.arr[idx]
#             idx=(idx-1)//2
#         return
    
#     def go_down(self):
#         idx=0
#         self.arr[idx],self.arr[-1]=self.arr[-1],self.arr[idx]
#         self.arr.pop()
#         while idx<len(self.arr)//2:
#             left=idx*2+1
#             right=idx*2+2
#             if right<len(self.arr) and self.arr[right]<self.arr[left]:
#                 tmp=right
#             else:
#                 tmp=left
#             if self.arr[tmp]<self.arr[idx]:
#                 self.arr[tmp],self.arr[idx]=self.arr[idx],self.arr[tmp]
#                 idx=tmp
#             else:
#                 break
#         return



# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.mheap=minheap()
#         self.k=k
#         for i,x in enumerate(nums):
#             self.mheap.push(x)
#             if self.mheap.size()>k:
#                 self.mheap.pop()
        

#     def add(self, val: int) -> int:
#         if self.mheap.size()==self.k and val<=self.mheap.top():
#             return self.mheap.top()
#         self.mheap.push(val)
#         if self.mheap.size()>self.k:
#             self.mheap.pop()
        
#         return self.mheap.top()


# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.kth_nums = []
        self.k = k

        for i in nums:
            if len(self.kth_nums) < k:
                heapq.heappush(self.kth_nums, i)
            else:
                heapq.heappushpop(self.kth_nums, i)


    def add(self, val: int) -> int:
        if len(self.kth_nums) < self.k:
            heapq.heappush(self.kth_nums, val)
        else:
            heapq.heappushpop(self.kth_nums, val)

        return self.kth_nums[0]