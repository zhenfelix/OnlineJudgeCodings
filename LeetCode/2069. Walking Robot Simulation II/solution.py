dxy = [(0,-1),(1,0),(0,1),(-1,0)]
dirs = ["South","East","North","West"]

class Robot:

    def __init__(self, width: int, height: int):
        self.tot = (width-1+height-1)*2
        self.w = width
        self.h = height
        self.k = 0
        self.x = 0
        self.y = 0
        self.first = True


    def move(self, num: int) -> None:
        self.first = False
        num = num%self.tot
        for i in range(num):
            dx, dy = dxy[self.k]
            if self.x+dx >= self.w or self.x+dx < 0 or self.y+dy >= self.h or self.y+dy < 0:
                self.k = (self.k+1)%4
                dx, dy = dxy[self.k]
            self.x += dx 
            self.y += dy 


    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.first:
            return "East"
        return dirs[self.k]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

