class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        for cur in costs:
            if coins < cur:
                break
            coins -= cur
            cnt += 1
        return cnt
