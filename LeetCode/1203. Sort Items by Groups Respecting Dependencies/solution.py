# from collections import Counter, defaultdict, deque
# import heapq

# class Solution:
#     def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
 
#         gGroup, gItem = defaultdict(list), defaultdict(list)
#         cntGroup, cntItem = Counter(), Counter()
#         g2item = defaultdict(set)
#         gcnt = m
#         for idx, g in enumerate(group):
#             if g == -1:
#                 group[idx] = gcnt
#                 g2item[gcnt].add(idx)
#                 gcnt += 1
#             else:
#                 g2item[g].add(idx)
                
#         for idx, items in enumerate(beforeItems):
#             for item in items:
#                 if group[idx] != group[item]:
#                     gGroup[group[item]].append(group[idx])
#                     cntGroup[group[idx]] += 1
#                 else:
#                     gItem[item].append(idx)
#                     cntItem[idx] += 1
                
                
#         qGroup = deque()
#         # print(cntGroup)
#         for j in range(gcnt):
#             if cntGroup[j] == 0:
#                 qGroup.append(j)
#         # print(qGroup)
#         res = []
#         while qGroup:
#             tmpGroup = qGroup.popleft()
#             gcnt -= 1
#             qItem = deque()
#             for item in g2item[tmpGroup]:
#                 if cntItem[item] == 0:
#                     qItem.append(item)
#             while qItem:
#                 tmp = qItem.popleft()
#                 res.append(tmp)
#                 g2item[tmpGroup].remove(tmp)
#                 for nxt in gItem[tmp]:
#                     cntItem[nxt] -= 1
#                     if cntItem[nxt] == 0:
#                         qItem.append(nxt)
#             if len(g2item[tmpGroup]) > 0:
#                 return []
            
#             for nxtGroup in gGroup[tmpGroup]:
#                 cntGroup[nxtGroup] -= 1
#                 if cntGroup[nxtGroup] == 0:
#                     qGroup.append(nxtGroup)
        
#         if gcnt > 0:
#             return []
#         return res
                

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        gs = [[] for _ in range(m)]
        for i, g in enumerate(group):
            if g == -1:
                group[i] = len(gs)
                gs.append([i])
            else: gs[g].append(i)
        m = len(gs)

        gnx = [set() for _ in range(m)]
        gid = [0 for _ in range(m)]
        inx = [set() for _ in range(n)]
        iid = [0 for _ in range(n)]

        for i, bf in enumerate(beforeItems):
            for j in bf:
                if group[i] != group[j]:
                    if group[i] not in gnx[group[j]]:
                        gnx[group[j]].add(group[i])
                        gid[group[i]] += 1
                else:
                    if i not in inx[j]:
                        inx[j].add(i)
                        iid[i] += 1
        
        def toposort(groups, nexts, indegrees):
            q = [i for i in groups if indegrees[i] == 0]
            ans = []
            while q:
                i = q.pop()
                ans.append(i)
                for j in nexts[i]:
                    indegrees[j] -= 1
                    if indegrees[j] == 0:
                        q.append(j)
            return ans if len(ans) == len(groups) else []
        
        gsort = toposort(range(m), gnx, gid)
        if not gsort: return []
        ans = []
        for g in gsort:
            if not gs[g]: continue
            t = toposort(gs[g], inx, iid)
            if not t: return []
            ans.extend(t)
        return ans
                    
            
        
        