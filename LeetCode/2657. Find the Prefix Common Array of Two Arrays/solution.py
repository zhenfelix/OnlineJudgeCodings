class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        cc = Counter()
        cnt = 0
        for a, b in zip(A,B):
            cc[a] += 1
            cc[b] += 1
            if cc[a] == 2:
                cnt += 1
            if cc[b] == 2:
                cnt += 1
            if a == b:
                cnt -= 1
            C.append(cnt)
        return C