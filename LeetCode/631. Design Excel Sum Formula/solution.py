class Excel:

    def __init__(self, H: int, W: str):
        self.data = collections.defaultdict(int)
        self.mp = collections.defaultdict(list)


    def set(self, r: int, c: str, v: int) -> None:
        if (r,c) in self.mp:
            del self.mp[r,c]
        self.data[r,c] = v
        

    def get(self, r: int, c: str) -> int:
        if (r,c) in self.mp:
            return self.sum_(r,c)
        return self.data[r,c]
        

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        self.mp[r,c] = strs
        return self.sum_(r,c)

    def sum_(self, r, c):
        sums = 0
        for ch in self.mp[r,c]:
            ch = ch.split(':')
            if len(ch) == 1:
                row, col = int(ch[0][1:]), ch[0][0]
                sums += self.get(row, col)
            else:
                row1, col1 = int(ch[0][1:]), ch[0][0]
                row2, col2 = int(ch[1][1:]), ch[1][0]
                for row in range(row1,row2+1):
                    col = col1
                    while col <= col2:
                        sums += self.get(row, col)
                        col = chr(ord(col)+1)
        return sums



        


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)