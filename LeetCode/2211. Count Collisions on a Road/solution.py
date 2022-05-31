class Solution:
    def countCollisions(self, directions: str) -> int:
        r, cnt, collide = 0, 0, False
        for ch in directions:
            if ch == 'R':
                r += 1
            elif ch == 'S':
                cnt += r 
                r = 0
                collide = True
            elif ch == 'L':
                if r > 0:
                    cnt += r+1
                    r = 0
                    collide = True
                elif collide:
                    cnt += 1
                    collide = True
        return cnt
