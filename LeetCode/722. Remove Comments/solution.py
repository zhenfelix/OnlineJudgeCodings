# class Solution:
#     def removeComments(self, source: List[str]) -> List[str]:
#       cnt = 0
#       idx = (-1,-1)
#       new_source = []
#       for i, line in enumerate(source):
#         if cnt == 0:
#             new_source.append("")
#         for j, ch in enumerate(line):
#           if cnt == 0 and j+1 < len(line) and line[j]+line[j+1] == "//":
#             break
#           elif cnt == 0 and j+1 < len(line) and line[j]+line[j+1] == "/*":
#             cnt += 1
#             idx = (i,j)
#           elif cnt == 1 and j-2 >= 0 and line[j-1]+line[j] == "*/" and (i,j-2) != idx:
#             cnt -= 1
#             idx = (-1,-1)
#             continue
#           if cnt == 0:
#             new_source[-1] += ch
#       return [line for line in new_source if line]

class Solution(object):
    def removeComments(self, source):
        in_block = False
        ans = []
        for line in source:
            i = 0
            if not in_block:
                newline = []
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == '//':
                    break
                elif not in_block:
                    newline.append(line[i])
                i += 1
            if newline and not in_block:
                ans.append("".join(newline))

        return ans

