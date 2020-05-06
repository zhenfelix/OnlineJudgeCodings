# class Solution:
#     def lengthLongestPath(self, input: str) -> int:
#         cur, res, i, n, depth = 0, 0, 0, len(input), 1
#         st, isfile = [0], [False]
#         while i < n:
#             if input[i] == "\n":
#                 depth = 1
#                 i += 1
#                 while input[i] == "\t":
#                     depth += 1
#                     i += 1
#                 while depth <= len(st):
#                     cur -= st.pop()
#                     isfile.pop()
#                 while depth > len(st):
#                     st.append(0)
#                     isfile.append(False)
#             cur += 1
#             st[-1] += 1
#             if input[i] == '.':
#                 isfile[-1] = True
#             # print(st,i)
#             if isfile[-1]:
#                 res = max(res,cur+len(st)-1)
#             i += 1
#         return res

class Solution:
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen

