class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        cur = capacity
        for i, c in enumerate(plants):
            if cur < c:
                res += 2*i 
                cur = capacity
            res += 1
            cur -= c 
        return res 

