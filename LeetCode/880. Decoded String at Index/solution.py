# class Solution:
#     def decodeAtIndex(self, S: str, K: int) -> str:
#         st = [(0,"")]
#         for s in S:
#             # print(st)
#             sz, ch = st[-1]
#             if s.isdigit():
#                 st.append((sz*int(s),s))
#             else:
#                 st.append((sz+1,s))
#             while st[-1][0] >= K:
#                 # print(K,st)
#                 sz, ch = st.pop()
#                 if sz == K:
#                     if ch.isdigit():
#                         K //= int(ch)
#                     else:
#                         return ch
#                 else:
#                     if K%st[-1][0] != 0:
#                         K %= st[-1][0] 
#                     else:
#                         K = st[-1][0]
#         return ""

class Solution(object):
    def decodeAtIndex(self, S, K):
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N //= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1

# class Solution(object):
#     def decodeAtIndex(self, S, K):
#         size = 0
#         # Find size = length of decoded string
#         for c in S:
#             if c.isdigit():
#                 size *= int(c)
#             else:
#                 size += 1

#         for c in reversed(S):
#             K %= size
#             if K == 0 and c.isalpha():
#                 return c

#             if c.isdigit():
#                 size //= int(c)
#             else:
#                 size -= 1