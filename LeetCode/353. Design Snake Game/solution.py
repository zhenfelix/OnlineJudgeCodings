# from collections import deque

# class SnakeGame:

#     def __init__(self, width: int, height: int, food: List[List[int]]):
#         """
#         Initialize your data structure here.
#         @param width - screen width
#         @param height - screen height 
#         @param food - A list of food positions
#         E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
#         """
#         self.food = [(f[0],f[1]) for f in food[::-1]]
#         self.width = width
#         self.height = height
#         self.body = deque()
#         self.visited = set()
#         self.body.append((0,0))
#         self.visited.add((0,0))
#         self.delta = {'U':(-1,0),'L':(0,-1),'R':(0,1),'D':(1,0)}
#         self.score = 0
        

#     def move(self, direction: str) -> int:
#         """
#         Moves the snake.
#         @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
#         @return The game's score after the move. Return -1 if game over. 
#         Game over when snake crosses the screen boundary or bites its body.
#         """
#         # print(self.body)
#         # print(self.visited)
#         # print(direction)
#         x, y = self.body[-1][0]+self.delta[direction][0], self.body[-1][1]+self.delta[direction][1]
#         self.visited.remove(self.body[0])
#         if x >= self.height or x < 0 or y >= self.width or y < 0 or (x,y) in self.visited:
#             return -1
#         self.visited.add((x,y))
#         self.body.append((x,y))
#         if self.food and (x,y) == self.food[-1]:
#             self.food.pop()
#             self.score += 1
#             self.visited.add(self.body[0])
#         else:
#             self.body.popleft()
            
#         return self.score


# # Your SnakeGame object will be instantiated and called as such:
# # obj = SnakeGame(width, height, food)
# # param_1 = obj.move(direction)



# class SnakeGame:

#     def __init__(self, width: int, height: int, food: List[List[int]]):
#         """
#         Initialize your data structure here.
#         @param width - screen width
#         @param height - screen height 
#         @param food - A list of food positions
#         E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
#         """
#         self.food = [(f[0],f[1]) for f in food[::-1]]
#         self.width = width
#         self.height = height
#         self.body = [(0,0)]
#         self.delta = {'U':(-1,0),'L':(0,-1),'R':(0,1),'D':(1,0)}
#         self.score = 0
        

#     def move(self, direction: str) -> int:
#         """
#         Moves the snake.
#         @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
#         @return The game's score after the move. Return -1 if game over. 
#         Game over when snake crosses the screen boundary or bites its body.
#         """
#         # print(self.body)
#         # print(direction)
#         x, y = self.body[-1][0]+self.delta[direction][0], self.body[-1][1]+self.delta[direction][1]
#         if x >= self.height or x < 0 or y >= self.width or y < 0 or (x,y) in self.body[1:]:
#             return -1
#         self.body.append((x,y))
#         if self.food and (x,y) == self.food[-1]:
#             self.food.pop()
#             self.score += 1
#         else:
#             self.body = self.body[1:]
#         return self.score


# # Your SnakeGame object will be instantiated and called as such:
# # obj = SnakeGame(width, height, food)
# # param_1 = obj.move(direction)


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.food = [(f[0],f[1]) for f in food[::-1]]
        self.width = width
        self.height = height
        self.body = [(0,0)]
        self.delta = {'U':(-1,0),'L':(0,-1),'R':(0,1),'D':(1,0)}
        self.score = 0
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # print(self.body)
        # print(direction)
        x, y = self.body[-1][0]+self.delta[direction][0], self.body[-1][1]+self.delta[direction][1]
        if x >= self.height or x < 0 or y >= self.width or y < 0:
            return -1
        
        if self.food and (x,y) == self.food[-1]:
            self.food.pop()
            self.score += 1
        else:
            self.body = self.body[1:]
            if (x,y) in self.body:
                return -1
        self.body.append((x,y))
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

