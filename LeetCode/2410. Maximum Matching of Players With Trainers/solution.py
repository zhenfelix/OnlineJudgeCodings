class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans = 0
        i, j = 0, 0
        n, m = len(players), len(trainers)
        for j in range(m):
            if i >= n:
                break
            if players[i] <= trainers[j]:
                i += 1
                ans += 1
        return ans 