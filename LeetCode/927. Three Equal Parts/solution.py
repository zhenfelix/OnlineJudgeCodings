class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        cc = Counter(A)
        if cc[1]%3: return [-1,-1]
        if cc[1] == 0: return [0,2]
        k = cc[1]//3
        cnt = 0
        pos = []
        for i, a in enumerate(A):
            if a == 1:
                cnt += 1
                if (cnt-1)%k == 0:
                    pos.append(i)
        # print(k,pos)
        i, j, k = pos
        while k < len(A):
            if A[i] != A[k] or A[j] != A[k]:
                return [-1,-1]
            i, j, k = i+1, j+1, k+1
        return [i-1,j]