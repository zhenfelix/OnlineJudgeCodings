# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations = sorted(citations, key = lambda x: -x)
#         h = len(citations)
#         for i, citation in enumerate(citations):
#             if i+1 > citation:
#                 h = i
#                 break
#         return h


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0]*(n+1)
        for citation in citations:
            if citation > n:
                cnt[n] += 1
            else:
                cnt[citation] += 1
        res = n
        while res > 0:
            if cnt[res] >= res:
                return res
            res -= 1
            cnt[res] += cnt[res+1]
        return res