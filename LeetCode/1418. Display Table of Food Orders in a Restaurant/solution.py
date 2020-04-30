# class Solution:
#     def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
#         tfs = [(table,food) for _,table,food in orders]
#         cc = Counter(tfs)
#         foods = sorted(list(set([food for _,table,food in orders])))
#         tables = sorted(list(set([table for _,table,food in orders])), key = lambda x: int(x))
#         # print(foods)
#         # print(tables)
#         res = [["Table"]+foods]
#         for table in tables:
#             res.append([table])
#             for food in foods:
#                 res[-1].append(str(cc[table,food]))
#         return res



import collections
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        desk = collections.defaultdict(collections.Counter)
        meal = set()
        for _, table, food in orders:
            meal.add(food)
            desk[table][food] += 1
        foods = sorted(meal)
        result = [['Table'] + [food for food in foods]]
        for table in sorted(desk, key=int):
            result.append([table] + [str(desk[table][food]) for food in foods])
        return result