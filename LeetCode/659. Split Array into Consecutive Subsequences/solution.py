from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cc = Counter(nums)
        # print(cc)
        # print(sorted(zip(cc.keys(),cc.values())))
        endings = Counter()
        for num in nums:
            if not cc[num]:
                continue
            if endings[num-1] > 0:
            	cc[num] -= 1
            	endings[num] += 1
            	endings[num-1] -= 1
            else:
            	for i in range(3):
            	    if cc[num+i] > 0:
            	        cc[num+i] -= 1
            	    else:
            	        return False
            	endings[num+i] += 1
          
        return True

import heapq
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        endings = collections.defaultdict(list)
        for num in nums:
            if not endings[num-1]:
                heapq.heappush(endings[num], 1)
            else:
                sz = heapq.heappop(endings[num-1])
                heapq.heappush(endings[num], sz+1)
                
        # print(endings)
        if any(heapq.heappop(ending) < 3 for num, ending in endings.items() if ending):
            return False
            
        return True



class Solution(object):
	"""docstring for Solution"""
	def isPossible(self, nums):
	        left = collections.Counter(nums)
	        end = collections.Counter()
	        for i in nums:
	            if not left[i]: continue
	            left[i] -= 1
	            if end[i - 1] > 0:
	                end[i - 1] -= 1
	                end[i] += 1
	            elif left[i + 1] and left[i + 2]:
	                left[i + 1] -= 1
	                left[i + 2] -= 1
	                end[i + 2] += 1
	            else:
	                return False
	        return True