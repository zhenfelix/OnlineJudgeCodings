class Solution:
    def checkOnesSegment(self, s):
        return '01' not in s        

# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         for i in range(len(s)-1):
#             if s[i:i+2] == "01":
#                 return False
#         return True