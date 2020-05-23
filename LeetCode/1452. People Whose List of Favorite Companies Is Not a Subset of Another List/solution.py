# class Solution:
#     def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
#         com2people = defaultdict(list)
#         for i, coms in enumerate(favoriteCompanies):
#             for com in coms:
#                 com2people[com].append(i)
#         res = []
#         for k, v in com2people.items():
#             if len(v) == 1:
#                 res.append(v[0])
#         return sorted(res)

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(v) for v in favoriteCompanies]
        res, n = [], len(favoriteCompanies)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if favoriteCompanies[i] & favoriteCompanies[j] == favoriteCompanies[i]:
                    break
            else:
                res.append(i)
        return res