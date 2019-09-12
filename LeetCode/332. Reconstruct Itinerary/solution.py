import collections

# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         # visited = collections.Counter()
#         mp = collections.defaultdict(list)
#         for a, b in sorted(tickets)[::-1]:
#             mp[a].append(b)
#             # visited[(a, b)] += 1
        
#         # for k, v in mp.items():
#         #     mp[k] = sorted(v, reverse = False)
        
        
#         path = []
        
#         def dfs(node):
#             while mp[node]:
#                 dfs(mp[node].pop())
#             path.append(node)
            
#         dfs('JFK')
#         # print(path)
#         # path.append('JFK')
#         return path[::-1]

# class Solution:
#     """docstring for Solution"""
#     def findItinerary(self, tickets):
#         targets = collections.defaultdict(list)
#         for a, b in sorted(tickets)[::-1]:
#             targets[a] += b,
#         route = []
#         def visit(airport):
#             while targets[airport]:
#                 visit(targets[airport].pop())
#             route.append(airport)
#         visit('JFK')
#         return route[::-1]
            
        
class Solution:
	def findItinerary(self, tickets):
	    targets = collections.defaultdict(list)
	    for a, b in sorted(tickets)[::-1]:
	        targets[a] += b,
	    route, stack = [], ['JFK']
	    while stack:
	        while targets[stack[-1]]:
	            stack += targets[stack[-1]].pop(),
	        route += stack.pop(),
	    return route[::-1]