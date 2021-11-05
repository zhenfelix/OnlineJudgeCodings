class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b = 0, 0
        cnta, cntb = 0, 0
        for ch in colors:
            if ch == 'A':
                b += max(0, cntb-2)
                cntb = 0
                cnta += 1
            else:
                a += max(0, cnta-2)
                cnta = 0
                cntb += 1
        a += max(0, cnta-2)
        b += max(0, cntb-2)
        return a > b