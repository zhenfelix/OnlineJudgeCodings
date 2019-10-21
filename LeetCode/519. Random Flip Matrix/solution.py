class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.mp = {}
        self.cols = n_cols
        self.rows = n_rows
        self.len = n_cols*n_rows
        

    def flip(self) -> List[int]:
        # choice = random.randint(0,self.len-1)
        # x = choice
        x = random.randint(0,self.len-1)
        while x in self.mp:
            x = self.mp[x]
        row, col = x//self.cols, x%self.cols
        # self.mp[choice] = self.len-1
        self.mp[x] = self.len-1
        self.len -= 1
        return [row,col]
        

    def reset(self) -> None:
        n_cols, n_rows = self.cols, self.rows
        self.mp = {}
        self.len = n_cols*n_rows



# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()