# class Solution:
#     def rankTeams(self, votes: List[str]) -> str:
#         rk = defaultdict(int)
#         for vote in votes:
#             for i, ch in enumerate(vote):
#                 rk[ch,i] += 1
#         n = len(votes[0])
#         chs = list(set(map(lambda y: y[0],rk.keys())))
#         chs = sorted(chs, key=lambda y: [-rk[y,i] for i in range(n)]+[y])
#         return ''.join(chs)

class Solution:
    def rankTeams(self, votes):
        count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1
        return ''.join(sorted(votes[0], key=count.get))