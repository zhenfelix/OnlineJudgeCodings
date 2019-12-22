# class Solution:
#     def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
#         n = len(groupSizes)
#         arr = sorted([(groupSizes[i],i) for i in range(n)])
#         res = []
#         i = 0
#         while i < n:
#             res.append([])
#             for j in range(arr[i][0]):
#                 res[-1].append(arr[i+j][1])
#             i += arr[i][0]
#         return res


# class Solution:
#     def groupThePeople(self, groupSizes):
#         count = collections.defaultdict(list)
#         for i, size in enumerate(groupSizes):
#             count[size].append(i)
#         return [l[i:i + s]for s, l in count.items() for i in range(0, len(l), s)]        

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sizeToGroup, res = collections.defaultdict(list), []
        for i, size in enumerate(groupSizes):
            sizeToGroup[size].append(i)
            if len(sizeToGroup[size]) == size:
                res.append(sizeToGroup.pop(size))
        return res