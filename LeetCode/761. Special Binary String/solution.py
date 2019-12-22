# class Solution:
#     def makeLargestSpecial(self, S: str) -> str:
#         # print(S)
#         if S == "":
#             return S
#         n = len(S)
#         pre, idx, cnt = 0, 0, 0
#         st = []
#         while idx < n:
#             if S[idx] == "1":
#                 cnt += 1
#             else:
#                 cnt -= 1
#             idx += 1
#             if cnt == 0:
#                 st.append((pre,idx))
#                 pre = idx
#         if len(st) == 1:
#             # if S[1] == "0":
#             #     return S
#             return "1"+self.makeLargestSpecial(S[1:-1])+"0"
#         return "".join(sorted(map(lambda x: self.makeLargestSpecial(S[x[0]:x[1]]),st))[::-1])

class Solution:
    def makeLargestSpecial(self, S):
            count = i = 0
            res = []
            for j, v in enumerate(S):
                count = count + 1 if v=='1' else count - 1
                if count == 0:
                    res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                    i = j + 1
            return ''.join(sorted(res)[::-1])