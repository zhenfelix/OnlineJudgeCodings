class Excel:

    def __init__(self, height: int, width: str):
        # self.height, self.width = height, ord(width)-ord('A')
        self.mat = defaultdict(int)
        self.child = defaultdict(Counter)

    @cache
    def dfs(self, r, c):
        if len(self.child[r,c]) == 0:
            return self.mat[r,c]
        return sum(self.dfs(nr,nc)*cnt for (nr,nc), cnt in self.child[r,c].items())

    def set(self, r: int, c: str, val: int) -> None:
        self.mat[r,c] = val
        self.child[r,c].clear()

    def get(self, r: int, c: str) -> int:
        self.dfs.cache_clear()
        return self.dfs(r,c)


    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.dfs.cache_clear()
        self.child[row,column].clear()
        def process(num):
            r, c = int(num[1:]), num[0]
            return r, c
        for s in numbers:
            if ':' not in s:
                r, c = process(s)
                self.child[row,column][r,c] += 1
            else:
                a, b = s.split(':')
                r_lo, c_lo = process(a)
                r_hi, c_hi = process(b)
                for i in range(r_lo, r_hi+1):
                    j = c_lo
                    while j <= c_hi:
                        self.child[row,column][i,j] += 1
                        j = chr(ord(j)+1)
        return self.dfs(row,column)





# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)



# brute force solution
# class Excel:

#     def __init__(self, H: int, W: str):
#         self.data = collections.defaultdict(int)
#         self.mp = collections.defaultdict(list)


#     def set(self, r: int, c: str, v: int) -> None:
#         if (r,c) in self.mp:
#             del self.mp[r,c]
#         self.data[r,c] = v
        

#     def get(self, r: int, c: str) -> int:
#         if (r,c) in self.mp:
#             return self.sum_(r,c)
#         return self.data[r,c]
        

#     def sum(self, r: int, c: str, strs: List[str]) -> int:
#         self.mp[r,c] = strs
#         return self.sum_(r,c)

#     def sum_(self, r, c):
#         sums = 0
#         for ch in self.mp[r,c]:
#             ch = ch.split(':')
#             if len(ch) == 1:
#                 row, col = int(ch[0][1:]), ch[0][0]
#                 sums += self.get(row, col)
#             else:
#                 row1, col1 = int(ch[0][1:]), ch[0][0]
#                 row2, col2 = int(ch[1][1:]), ch[1][0]
#                 for row in range(row1,row2+1):
#                     col = col1
#                     while col <= col2:
#                         sums += self.get(row, col)
#                         col = chr(ord(col)+1)
#         return sums



        


# # Your Excel object will be instantiated and called as such:
# # obj = Excel(H, W)
# # obj.set(r,c,v)
# # param_2 = obj.get(r,c)
# # param_3 = obj.sum(r,c,strs)