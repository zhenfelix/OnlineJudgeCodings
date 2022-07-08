class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n, m = cont[-1], 1
        cont = cont[:-1]
        for v in cont[::-1]:
            n, m = m, n
            n += m*v
        return [n,m]
        
