# class Solution:
#     def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
#         croak = "croak"
#         res = 0
#         s = list(map(lambda x: croak.index(x), croakOfFrogs))
#         cc = [0]*5
#         for x in s:
#             cc[x] += 1
#             if x > 0:
#                 cc[x-1] -= 1
#                 if cc[x-1] < 0:
#                     return -1
#             print(cc)
#             res = max(res,sum(cc[:4]))
#         if any(cc[i] != 0 for i in range(4)):
#             return -1
#         return res

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        res = 0
        state = [0]*5
        for ch in croakOfFrogs:
            cur = "croak".index(ch)
            pre = (cur-1)%5
            state[cur] += 1
            state[pre] -= 1
            if state[pre] < 0:
                if pre == 4:
                    res += 1
                    state[pre] += 1
                else:
                    return -1
        return res if state[-1] == res else -1