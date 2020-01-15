class Solution:
    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    #     presums = [0]
    #     for a in arr:
    #         presums.append(presums[-1]^a)
    #     res = []
    #     for left, right in queries:
    #         res.append(presums[right+1]^presums[left])
    #     return res

    def xorQueries(self, A, queries):
        for i in xrange(len(A) - 1):
            A[i + 1] ^= A[i]
        return [A[j] ^ A[i - 1] if i else A[j] for i, j in queries]