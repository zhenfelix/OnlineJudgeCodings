class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money == children*8:
            return children
        if money-(children-1)*8 > 0 and money-(children-1)*8 != 4:
            return children-1
        for i in range(children-1)[::-1]:
            if money-i*8 >= children-i:
                return i  
        return -1