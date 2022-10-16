class LUPrefix:

    def __init__(self, n: int):
        self.visited = set()
        self.reach = 0


    def upload(self, video: int) -> None:
        self.visited.add(video)


    def longest(self) -> int:
        while self.reach+1 in self.visited:
            self.reach += 1
        return self.reach



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()