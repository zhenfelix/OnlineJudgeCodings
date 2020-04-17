class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res, n = 0, len(rating)
        for i in range(n):
            leftp, leftn = 0, 0
            for j in range(i):
                if rating[j] < rating[i]:
                    leftn += 1
                else:
                    leftp += 1
            rightp, rightn = 0, 0
            for j in range(i+1,n):
                if rating[i] < rating[j]:
                    rightp += 1
                else:
                    rightn += 1
            res += leftn*rightp + leftp*rightn
        return res