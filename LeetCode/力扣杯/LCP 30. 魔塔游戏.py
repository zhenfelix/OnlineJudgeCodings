class Solution:
    def magicTower(self, nums: List[int]) -> int:
        cur, monster, res = 1, 0, 0
        q = []
        for x in nums:
            cur += x
            if x < 0:
                heapq.heappush(q,x)
            while q and cur <= 0:
                m = heapq.heappop(q)
                cur -= m 
                monster += m 
                res += 1
            if cur <= 0:
                return -1
        if cur + monster <= 0:
            return -1
        return res 
