# class Solution:
#     def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
#         n = len(s)
#         res, mp = 0, collections.Counter()
#         for i in range(n):
#             cc = collections.Counter()
#             for j in range(i,min(i+minSize-1,n)):
#                 cc[s[j]] += 1
#                 if len(cc) > maxLetters:
#                     break
#             else:
#                 for j in range(min(i+minSize-1,n),min(i+maxSize,n)):
#                     cc[s[j]] += 1
#                     if len(cc) > maxLetters:
#                         break
#                     mp[s[i:j+1]] += 1
#                     res = max(res,mp[s[i:j+1]])
#             # print(i,mp)
#         return res


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter, n = collections.Counter(), len(s)
        for i in range(n - minSize + 1):
            if len(set(s[i:i + minSize])) <= maxLetters:
                counter[s[i:i + minSize]] += 1
        return max(counter.values()) if counter else 0