class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for region in regions:
            for i in range(1,len(region)):
                parent[region[i]] = region[0]
        chain = set([region1])
        while region1 in parent:
            region1 = parent[region1]
            chain.add(region1)
        while region2 not in chain:
            region2 = parent[region2]
        return region2


# class Solution:
#     def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
#         mp = collections.defaultdict(list)
#         children = set()
#         for region in regions:
#             for r in region[1:]:
#                 mp[region[0]].append(r)
#                 children.add(r)

#         rt = None
#         for region in regions:
#             if region[0] not in children:
#                 rt = region[0]
#                 break

#         def lca(root):
#             if root in [region1, region2]:
#                 return root
#             r = None
#             for child in mp[root]:
#                 tmp = lca(child)
#                 if tmp:
#                     if r:
#                         return root
#                     r = tmp
#             return r

#         return lca(rt)