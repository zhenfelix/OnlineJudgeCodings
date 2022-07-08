class Solution:
    def canReceiveAllSignals(self, intervals: List[List[int]]) -> bool:
        pre = -float('inf')
        for s, e in sorted(intervals):
            if s < pre:
                return False
            pre = max(pre, e)
        return True