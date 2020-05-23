# class Solution:
#     def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
#         start, end = Counter(startTime), Counter(endTime)
#         res = 0
#         for i in range(queryTime+1):
#             res -= end[i-1]
#             res += start[i]
#         return res

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))