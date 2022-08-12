class Solution:
    def solveEquation(self, equation: str) -> str:
        cf, val = 0, 0
        flag = 1
        positive = 1
        num = ''
        equation += '+'
        for ch in equation:
            
            if not ch.isdigit():
                if ch == 'x':
                    cf += positive*flag*(int(num) if num else 1)
                else:
                    val += positive*flag*(int(num) if num else 0)
                if ch == '=':
                    flag = -1
                num = ''
                positive = 1
            if ch.isdigit():
                num += ch
            if ch == '-':
                positive = -1
            # print(ch,cf,val)
        if cf == 0:
            return 'Infinite solutions' if val == 0 else 'No solution'
        return 'x='+str(-val//cf)