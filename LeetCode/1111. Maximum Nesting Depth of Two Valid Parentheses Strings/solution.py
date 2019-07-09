class Solution:
    # def maxDepthAfterSplit(self, seq: str) -> List[int]:
    #     flag = []
    #     A, B = 0, 0
    #     ans = [0]*len(seq)
    #     for i, s in enumerate(seq):
    #         if s == '(':
    #             if A <= B:
    #                 A += 1
    #                 ans[i] = 0
    #                 flag.append(0)
    #             else:
    #                 B += 1
    #                 ans[i] = 1
    #                 flag.append(1)
    #         else:
    #             if flag[-1] == 0:
    #                 A -= 1
    #                 ans[i] = 0
    #                 flag.pop()
    #             else:
    #                 B -= 1
    #                 ans[i] = 1
    #                 flag.pop()
    #     return ans
    
    def maxDepthAfterSplit(self, seq):
        A = B = 0
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            v = 1 if c == '(' else -1
            if (v > 0) == (A < B):
                A += v
            else:
                B += v
                res[i] = 1
        return res