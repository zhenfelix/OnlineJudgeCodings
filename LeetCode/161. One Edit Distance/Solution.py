# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         if len(s) == len(t):
#             if any(s[:i]==t[:i] and s[i+1:]==t[i+1:] and s[i] != t[i] for i in range(len(s))):
#                 return True
#         elif len(s)-len(t) in [-1,1]:
#             if len(s) < len(t):
#                 t, s = s, t
#             if any(s[:i]+s[i+1:] == t for i in range(len(s))):
#                 return True
#         return False
    
    
# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         diff = 0
#         if len(s) == len(t):
#             for i in range(len(s)):
#                 if s[i] != t[i]:
#                     diff += 1
#                     if diff > 1:
#                         return False
#             return diff == 1
        
#         elif len(s)-len(t) in [-1,1]:
#             if len(s) < len(t):
#                 t, s = s, t
#             i, j = 0, 0
#             while i < len(s) and j < len(t):
#                 if s[i] != t[j]:
#                     i += 1
#                     diff += 1
#                     if diff > 1:
#                         return False
#                 else:
#                     i += 1
#                     j += 1
#             return diff == 1 or i < len(s)
#         return False



class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if s == t: return False
        if abs(n1 - n2) > 1: return False
        if not s or not t: return True
        if n1 > n2: return self.isOneEditDistance(t, s)
        if n1 == n2:
            i = 0
            not_same = 0
            while i < n1:
                if s[i] != t[i]:
                    not_same += 1
                if not_same > 1:
                    return False
                i += 1
            return True
        else:
            i = 0
            j = 0
            not_same = 0
            while i < n1 and j < n2:
                if s[i] != t[j]:
                    j += 1
                    not_same += 1
                if not_same > 1 : return False
                if s[i] == t[j]:
                    i += 1
                    j += 1
            return i == n1 and (not_same + n2 - j) == 1
