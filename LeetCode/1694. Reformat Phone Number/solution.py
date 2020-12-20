class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        n = len(number)
        res = ''
        i = 0
        while n-i > 4:
            res += number[i:i+3]
            res += '-'
            i += 3
        if n-i == 4:
            res += number[i:i+2] + '-' + number[i+2:]
        else:
            res += number[i:]
        return res