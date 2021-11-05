class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int,date.split('-'))
        month = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(1,m):
            d += month[i-1]
            if i == 2 and y%4 == 0:
                d += 1
        return d