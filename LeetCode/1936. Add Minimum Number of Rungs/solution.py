class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        pre, cnt = 0, 0
        for cur in rungs:
            cnt += (cur-pre-1)//dist
            pre = cur
        return cnt