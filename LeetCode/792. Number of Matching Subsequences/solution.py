# import collections

# class Solution:
# 	def isSubsequence(self, s):
# 	    def lower_bound(nums, target):
# 	        left, right = 0, len(nums)-1
# 	        while left <= right:
# 	            mid = (left+right)//2
# 	            if nums[mid] > target:
# 	                right = mid-1
# 	            else:
# 	                left = mid+1
# 	        return left

# 	    pre = -1
# 	    for ch in s:
# 	        j = lower_bound(self.mp[ch], pre)
# 	        if j == len(self.mp[ch]):
# 	            return False
# 	        pre = self.mp[ch][j]
# 	    return True

# 	def numMatchingSubseq(self, S: str, words: List[str]) -> int:
# 	    self.mp = collections.defaultdict(list)
# 	    for i, ch in enumerate(S):
# 	        self.mp[ch].append(i)
# 	    cc = 0
# 	    for word in words:
# 	    	if self.isSubsequence(word):
# 	    		cc += 1
# 	    return cc


# from collections import deque

# class Solution:
#     def numMatchingSubseq(self, S: str, words: List[str]) -> int:
#         q = deque()
#         n = len(words)
#         for i in range(n):
#             q.append([i,0])
            
#         for _, ch in enumerate(S):
#             m = len(q)
#             for _ in range(m):
#                 front = q.popleft()
#                 if words[front[0]][front[1]] == ch:
#                     front[1] += 1
#                     if front[1] == len(words[front[0]]):
#                         continue
#                 q.append(front.copy())

#         return len(words)-len(q)

class Solution:
    def numMatchingSubseq(self, S, words):
        waiting = collections.defaultdict(list)
        # for w in words:
        #     waiting[w[0]].append(iter(w[1:]))
        for it in map(iter, words):
                waiting[next(it)].append(it)
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])