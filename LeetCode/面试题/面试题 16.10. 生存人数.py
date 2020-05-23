class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        birth = Counter(birth)
        death = Counter(death)
        res, year, cnt = 0, 0, 0
        for i in range(1900,2001):
            cnt += birth[i]
            if cnt > res:
                res, year = cnt, i 
            cnt -= death[i]
        return year