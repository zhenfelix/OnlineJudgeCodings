class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        winner, loser = defaultdict(int), defaultdict(int)
        for w, l in matches:
            players.add(w)
            players.add(l)
            winner[w] += 1
            loser[l] += 1
        return [sorted([p for p in players if loser[p] == 0]), sorted([p for p in players if loser[p] == 1])]