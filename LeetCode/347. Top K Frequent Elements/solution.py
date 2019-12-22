# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         cnt = collections.Counter(nums)
#         q = [(-v,k) for k,v in cnt.items()]
#         heapq.heapify(q)
#         res = []
#         for _ in range(k):
#             res.append(heapq.heappop(q)[1])
#         return res


# class Solution:
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """ 
#         count = collections.Counter(nums)   
#         return heapq.nlargest(k, count.keys(), key=count.get) 

# import functools
# class Solution:
#     def topKFrequent(self, nums, k):
#         bucket = [[] for _ in nums]
#         for num, freq in collections.Counter(nums).items():
#             bucket[-freq].append(num)
#         return list(functools.reduce(lambda a,b: a+b, bucket))[:k]


class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        for num, freq in collections.Counter(nums).items():
            bucket[-freq].append(num)
        return list(itertools.chain(*bucket))[:k]