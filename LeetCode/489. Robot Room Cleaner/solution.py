# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        delta = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()

        def dfs(x,y,state):
            robot.clean()
            visited.add((x,y))
            for i in range(4):
                if (x+delta[state][0],y+delta[state][1]) not in visited and robot.move():
                    dfs(x+delta[state][0],y+delta[state][1],state)
                    robot.turnRight()
                else:
                    robot.turnLeft()
                state -= 1
                state %= 4
            for i in range(2):
                robot.turnLeft()
            robot.move()
            return

        dfs(0,0,0)
        return


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        dxy = [(1,0),(0,-1),(-1,0),(0,1)]
        x, y, cur = 1, 3, 2

        def check():
            nonlocal x, y, cur
            return (x+dxy[cur][0],y+dxy[cur][1]) not in visited and robot.move()

        def dfs():
            nonlocal x, y, cur
            # print(x,y,dxy[cur])
            visited.add((x,y))
            robot.clean()
            # if (x,y) == (2,0):
            #     return 
            # pre = cur
            for _ in range(4):
                # if (x,y) == (2,0):
                #     return 
                if check():
                    x += dxy[cur][0]
                    y += dxy[cur][1]
                    # print("success move: {}".format((x,y)))
                    dfs()
                    robot.turnRight()
                    cur = (cur+1)%4
                else:
                    robot.turnLeft()
                    cur = (cur-1)%4
            robot.turnLeft()
            robot.turnLeft()
            cur = (cur+2)%4
            if robot.move():
                x = x+dxy[cur][0]
                y = y+dxy[cur][1]
            return 
        dfs()
        # robot.clean()
        # robot.move()
        # robot.clean()
        return