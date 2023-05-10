class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calc(player):
            n = len(player)
            ans = 0
            for i in range(n):
                if (i > 0 and player[i-1] == 10) or (i > 1 and player[i-2] == 10):
                    ans += player[i]*2
                else:
                    ans += player[i]
            return ans 
        p1 = calc(player1)
        p2 = calc(player2)
        if p1 == p2:
            return 0    
        if p1 > p2:
            return 1
        return 2 