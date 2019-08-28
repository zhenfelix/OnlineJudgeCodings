class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n = len(A)
        ans = [False]*n
        s = 0
        for idx, a in enumerate(A):
            s = (s*2+a)%5
            if s == 0:
                ans[idx] = True
        return ans