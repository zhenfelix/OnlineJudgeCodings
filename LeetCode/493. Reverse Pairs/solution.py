
# class Solution:
#     def update(self, tree, pos, val):
#         n = len(tree)-1
#         while pos <= n:
#             tree[pos] += val
#             pos += (pos & (-pos))
#         return

#     def sums(self, tree, pos):
#         res = 0
#         while pos > 0:
#             res += tree[pos]
#             pos -= (pos & (-pos))
#         return res

#     def query(self, tree, left, right):
#         return self.sums(tree,right)-self.sums(tree,left-1)


#     def reversePairs(self, nums: List[int]) -> int:
#         arr = sorted(set(nums))
#         n = len(arr)        
#         cnt = [0]*(n+1)
#         ans = 0

#         for num in nums:
#             idx = bisect.bisect_left(arr,2*num+1)
#             ans += self.query(cnt,idx+1,n)
#             idx = bisect.bisect_left(arr,num)
#             self.update(cnt,idx+1,1)
        
#         return ans

        
class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n
    
    def update(self, i, delta):
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

class Solution:
    def reversePairs(self, nums):
        new_nums = nums + [x * 2 for x in nums]
        sorted_set = sorted(list(set(new_nums)))
        tree = BIT(len(sorted_set))
        res = 0
        ranks = {}
        for i, n in enumerate(sorted_set):
            ranks[n] = i + 1
            
        for n in nums[::-1]:
            res += tree.query(ranks[n] - 1)
            tree.update(ranks[n * 2], 1)
        
        return res