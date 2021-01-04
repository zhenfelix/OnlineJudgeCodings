class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes.sort(key=lambda x: x[-1])
        while truckSize and boxTypes:
            cnt, cap = boxTypes.pop()
            res += cap*min(cnt,truckSize)
            truckSize = max(0,truckSize-cnt)
        return res 