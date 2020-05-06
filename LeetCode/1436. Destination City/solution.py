# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         A, B = set(), set()
#         for a, b in paths:
#             A.add(a)
#             B.add(b)
#         res = B-A
#         return res.pop()

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = map(set, zip(*paths))
        return (B - A).pop()

# Difference between zip(list) and zip(*list) [duplicate]
# https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist/29139418