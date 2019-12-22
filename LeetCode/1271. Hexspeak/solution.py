# class Solution:
#     def toHexspeak(self, num: str) -> str:
#         res = ""
#         tmp = hex(int(num))[2:]
#         mp = {'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','1':'I','0':'O'}
#         for ch in tmp:
#             if ch not in mp:
#                 return "ERROR"
#             res += mp[ch]
#         return res

class Solution:
    def toHexspeak(self, num: str) -> str:
        ans = ''
        s = hex(int(num)).upper()[2 :].replace('0', 'O').replace('1', 'I')
        for c in s:
            if c not in ('A', 'B', 'C', 'D', 'E', 'F', 'O', 'I'):
                return 'ERROR'
            ans += c
        return ans