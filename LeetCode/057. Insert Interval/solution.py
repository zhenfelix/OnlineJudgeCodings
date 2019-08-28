class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = [i for i in intervals if i[1] < newInterval[0]]
        right = [i for i in intervals if i[0] > newInterval[1]]
        if len(left)+len(right) != len(intervals):
            newInterval[0] = min(newInterval[0], intervals[len(left)][0])
            newInterval[1] = max(newInterval[1], intervals[len(intervals)-len(right)-1][1])
        return left + [newInterval] + right