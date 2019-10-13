# from collections import Counter, defaultdict

# class Solution:
#     def minTransfers(self, transactions: List[List[int]]) -> int:
#         persons = set()
#         debt = Counter()
#         for e in transactions:
#             debt[e[0]] += e[2]
#             debt[e[1]] -= e[2]
#             persons.add(e[0])
#             persons.add(e[1])

#         def dfs(cur,cnts):
#             if cnts >= ans[0]:
#                 return
#             if debt[cur] == 0:
#                 for person in persons:
#                     if debt[person] != 0:
#                         cur = person
#                         break
            
#             if debt[cur] == 0:
#                 ans[0] = min(ans[0],cnts)
#                 return
            
#             tmp = debt[cur]
#             for nxt in persons:
#                 if debt[nxt]*debt[cur] < 0:
#                     debt[cur] -= tmp
#                     debt[nxt] += tmp
#                     dfs(nxt,cnts+1)
#                     debt[nxt] -= tmp
#                     debt[cur] += tmp
#             return

#         ans = [float('inf')]
#         cc = 0
#         mp = defaultdict(list)
#         for k, v in debt.items():
#             if v != 0 and len(mp[-v]) > 0:
#                 cc += 1
#                 idx = mp[-v].pop()
#                 debt[idx] = 0
#                 debt[k] = 0
#                 # del debt[k]
#                 # del debt[idx]
#             elif v != 0:
#                 mp[v] += [k]

#         # print(debt)
#         dfs(transactions[0][0],cc)
#         return ans[0]


from collections import Counter, defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        persons = set()
        debt = Counter()
        for e in transactions:
            debt[e[0]] += e[2]
            debt[e[1]] -= e[2]
            persons.add(e[0])
            persons.add(e[1])

        ans = [float('inf')]
        cc = 0
        # mp = defaultdict(list)
        # for k, v in debt.items():
        #     if v != 0 and len(mp[-v]) > 0:
        #         cc += 1
        #         idx = mp[-v].pop()
        #         debt[idx] = 0
        #         debt[k] = 0
        #         # del debt[k]
        #         # del debt[idx]
        #     elif v != 0:
        #         mp[v] += [k]
        debt = list(debt.values())
        debt = [a for a in debt if a != 0]
        n = len(debt)

        def dfs(cur,cnts):
            if cnts >= ans[0]:
                return
            while cur < n and debt[cur] == 0:
                cur += 1
            
            if cur == n:
                ans[0] = min(ans[0],cnts)
                return
            
            for nxt in range(cur+1,n):
                if debt[nxt]*debt[cur] < 0:
                    debt[nxt] += debt[cur]
                    dfs(cur+1,cnts+1)
                    debt[nxt] -= debt[cur]
            return

        # print(debt)
        # print(cc)
        dfs(0,cc)
        return ans[0]
