class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1],x[0]))
        # print(intervals)
        cnt = 0
        first, second = -2, -1
        for left, right in intervals:
            if second < left:
                cnt += 2
                first, second = right-1, right
            elif first < left:
                cnt += 1
                first, second = min(second,right-1), right
            # print(left,right,first,second,cnt)
        return cnt
