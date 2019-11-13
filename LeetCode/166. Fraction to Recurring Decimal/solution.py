class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator < 0:
            denominator = -denominator
            numerator = - numerator

        a = str(abs(numerator)//denominator)
        if numerator < 0:
            a = '-'+a
        b = abs(numerator)%denominator
        if b == 0:
            return a

        # def dfs(mod, pos):
        #     if mod == 0:
        #         return -1, ""
        #     if mod in memo:
        #         return memo[mod], ""
        #     memo[mod] = pos
        #     repeat, postfix = dfs((mod%denominator)*10, pos+1)
        #     return repeat, str(mod//denominator)+postfix


        memo, pos, mod = {}, 0, b*10
        idx, decimal = -1, ""
        while mod:
            if mod in memo:
                idx = memo[mod]
                break
            else:
                memo[mod] = pos
                decimal += str(mod//denominator)
                mod = (mod%denominator)*10
                pos += 1

        
        if idx == -1:
            return a + '.' + decimal
        return a + '.' + decimal[:idx] + '(' + decimal[idx:] + ')'
