class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        packs = []
        for c, r in zip(capacity,rocks):
            packs.append(c-r)
        packs.sort()
        ans = 0
        for p in packs:
            if additionalRocks-p >= 0:
                ans += 1
                additionalRocks -= p  
            else:
                return ans 
        return ans 