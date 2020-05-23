class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        last = 0
        for t in target:
            if t != last+1:
                res += ['Push', 'Pop']*(t-last-1)
            res += ['Push']
            last = t 
        return res