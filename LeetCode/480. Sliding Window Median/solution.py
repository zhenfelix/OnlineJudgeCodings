# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         window = nums[:k]
#         window.sort()
#         res = []
#         for a,b in zip(nums,nums[k:]+[0]):
#             res.append((window[k//2]+window[~(k//2)])/2)
#             window.remove(a)
#             bisect.insort(window, b)
#         return res


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxHeap = []
        minHeap = []
        
        # Step 1: Heap Initialization
        # When there are 4 elements: we have 2 in maxHeap and 2 in minHeap
        # When there are 5 elements: we have 2 in maxHeap and 3 in minHeap
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))
        
        for _ in range(k - k//2):
            num, i = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, (-num, i))
        
        # Step 2: Sliding Window and Maintain Heap Balance
        ans = [(-maxHeap[0][0]+minHeap[0][0])/2.0] if k%2 == 0 else [minHeap[0][0]/1.0]
        for i in range(k, len(nums)):
            
            # always add the element to minHeap
            num, j = heapq.heappushpop(maxHeap, (-nums[i], i))
            heapq.heappush(minHeap, (-num, j))
            
            # Now check the inbalance
            if (nums[i-k], i-k) < minHeap[0]:
            # if nums[i-k] < minHeap[0][0]:
                # IMPORTANT: `if nums[i-k] < minHeap[0][0]` won't work!
                # EXPLANATION:
                # there could be a number valued at nums[i-k] in both minHeap and maxHeap
                # number to be removed in maxHeap, inbalance
                # transfer one element to maxHeap
                num, j = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-num, j))
            
            
            while minHeap and minHeap[0][1] <= i-k:
                heapq.heappop(minHeap)
            while maxHeap and maxHeap[0][1] <= i-k:
                heapq.heappop(maxHeap)
                
            print(minHeap)
            print(maxHeap)
            print(nums[i],nums[i-k],i-k)
            
            if k%2 == 0:
                ans.append((-maxHeap[0][0]+minHeap[0][0])/2.0)
            else:
                ans.append((minHeap[0][0])/1.0)            
        return ans
        

    
    
    
    
    
    
        