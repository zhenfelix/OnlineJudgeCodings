class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cc = collections.defaultdict(int)
        res, width = 0, sum(wall[0])
        for bricks in wall:
            x = 0
            for brick in bricks:
                x += brick
                if x == width:
                    continue
                cc[x] += 1
                res = max(res, cc[x])
        # print(cc)
        return len(wall) - res