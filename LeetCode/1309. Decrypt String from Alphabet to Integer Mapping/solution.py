class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = len(s)-1
        while i >= 0:
            if s[i] == "#":
                res.append(int(s[i-2:i]))
                i -= 3
            else:
                res.append(int(s[i]))
                i -= 1
        return "".join(map(lambda x: chr(ord('a')+x-1), res))[::-1]



# class Solution(object):
#     def freqAlphabets(self, s):
#         i = 0
#         ans = []
#         while i < len(s):
#             if i + 2 < len(s) and s[i+2] == '#':
#                 code = int(s[i:i+2])
#                 ans.append(chr(code + ord('a') - 1))
#                 i += 3
#             else:
#                 code = int(s[i])
#                 ans.append(chr(code + ord('a') - 1))
#                 i += 1
                
#         return "".join(ans)


class Solution:
    def freqAlphabets(self, s):
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))