class Solution:
    def mergeAlternately(self, w1, w2):
        return ''.join(a + b for a, b in zip_longest(w1, w2, fillvalue=''))        
    
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         res = ""
#         for a, b in itertools.zip_longest(word1,word2):
#             if a:
#                 res += a
#             if b:
#                 res += b
#         return res 