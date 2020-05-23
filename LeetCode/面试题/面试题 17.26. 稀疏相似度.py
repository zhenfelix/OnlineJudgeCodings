# class Solution:
#     def normal_round(self, n):
#         if n - math.floor(n) < 0.5:
#             return math.floor(n)
#         return math.ceil(n)

#     def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
#         n = len(docs)
#         docs = [set(doc) for doc in docs]
#         res = []
#         for i in range(n):
#             for j in range(i+1,n):
#                 p = len(docs[i]&docs[j])/len(docs[i]|docs[j])
#                 p = self.normal_round(p*10**4)/(10**4)
#                 if p > 0:
#                     res.append("{},{}: ".format(i,j) + '{0:0<6}'.format(p))
#         return res

class Solution:
    def normal_round(self, n):
        if n - math.floor(n) < 0.5:
            return math.floor(n)
        return math.ceil(n)


    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        dic1 = collections.defaultdict(list)
        for i, doc in enumerate(docs):
            for num in doc:
                dic1[num].append(i)
        dic2 = collections.defaultdict(int)
        for li in dic1.values():
            for p in range(len(li)):
                for q in range(p + 1, len(li)):
                    dic2[li[p], li[q]] += 1
        res = []
        # minn = 1e-9
        for (p, q), i in dic2.items():
            u = len(docs[p]) + len(docs[q]) - i
            res.append("{0:d},{1:d}: {2:.4f}".format(p, q, self.normal_round(i / u * 10**4)/(10**4)))
        return res