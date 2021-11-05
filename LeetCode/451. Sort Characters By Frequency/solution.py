# class Solution:
#     def frequencySort(self, s: str) -> str:
#         mp = {}
#         for ch in s:
#             if ch in mp:
#                 mp[ch] += 1
#             else:
#                 mp[ch] = 1
#         arr = []
#         for k, v in mp.items():
#             arr.append((k,v))
#         arr = sorted(arr, key = lambda x: -x[1])
#         ans = ""
#         for x in arr:
#             ans += x[0]*x[1]
#         return ans
            
        
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_set = set(s)
        table = []
        for val in s_set:
            table.append((val, s.count(val)))

        table.sort(key = lambda x: x[1], reverse = True) 

        return ''.join(map(lambda x: x[0] * x[1], table))


class Solution:
    def frequencySort(self, s: str) -> str:
        cc = Counter(s)
        arr = sorted([(-v,k) for k,v in cc.items()])
        # print(arr)
        # print([k*(-v) for v,k in arr])
        return ''.join([k*(-v) for v,k in arr])


class Solution:
    def frequencySort(self, s: str) -> str:
        cc = Counter(s)
        return ''.join(sorted(list(s), key = lambda x: (-cc[x], x)))