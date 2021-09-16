class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:
        mp = set([(x,y) for x, y in circles])
        valid = set()
        for i, j, k in toys:
            for dx in range(-10,11,1):
                for dy in range(-10,11,1):
                    x, y = i+dx, j+dy
                    # if (x,y) in mp:
                    #     print(i,j,k,x,y)
                    if (x,y) in mp and r >= k and (i-x)**2 + (j-y)**2 <= (r-k)**2:
                        valid.add((i,j))
                        
        return len(valid)



