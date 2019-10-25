# class Solution:
#     def canConvert(self, str1: str, str2: str) -> bool:
#         mp = {}
#         for i, ch in enumerate(str1):
#             if ch not in mp:
#                 mp[ch] = [i]
#             else:
#                 mp[ch] += [i]
#         ans = True
#         # print(mp)
#         for ch in "abcdefghijklmnopqrstuvwxyz":
#             if ch in mp:
#                 ch2 = str2[mp[ch][0]]
#                 # print("ch: ",ch)
#                 for idx in mp[ch]:
#                     if str2[idx] != ch2:
#                         ans = False
#                         break
#             if not ans:
#                 break
#         return ans

# class Solution:
#     def canConvert(self, str1: str, str2: str) -> bool:
#         def toSet(string):
#             arr = []
#             mp = {}
#             for idx, ch in enumerate(string):
#                 if ch not in mp:
#                     mp[ch] = len(arr)
#                     arr.append([idx])
#                 else:
#                     arr[mp[ch]].append(idx)
#             return arr,mp
#         arr1, mp1 = toSet(str1)
#         arr2, mp2 = toSet(str2)
#         n = len(str1)
#         hashArr = [0]*n
#         for idx, aa in enumerate(arr1):
#             for a in aa:
#                 hashArr[a] = idx
                
#         if len(arr1) == len(arr2) == 26 and str1 != str2:
#             return False
        
#         for idx, aa in enumerate(arr2):
#             for a in aa:
#                 if hashArr[a] < idx:
#                     return False
#                 elif hashArr[a] > idx:
#                     for x in arr1[hashArr[a]]:
#                         hashArr[x] = idx
#         return True

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        s1 = dict()
        for i, ch in enumerate(str1):
            if ch not in s1:
                s1[ch] = list()
            s1[ch].append(i)
        s2 = dict()
        for i, ch in enumerate(str2):
            if ch not in s2:
                s2[ch] = list()
            s2[ch].append(i)
        if len(s1) == len(s2) == 26 and str1 != str2:
            return False

        for k, v in s1.items():
            pivot = str2[v[0]]
            for pos in v:
                if str2[pos] != pivot:
                    return False

        return True


# from collections import Counter
# class Solution:
#     def canConvert(self, str1: str, str2: str) -> bool:
#         mp = {}
#         # cc1, cc2 = Counter(str1), Counter(str2)
#         # if len(cc1) < len(cc2):
#         #     return False
#         # elif len(cc1) == len(cc2)==26:
#         #     return str1 == str2
#         if len(Counter(str1)) == len(Counter(str2)) == 26 and str1 != str2:
#             return False
#         for i, ch in enumerate(str1):
#             if ch in mp and mp[ch] != str2[i]:
#                 return False
#             else:
#                 mp[ch] = str2[i]
#         return True

                    
        
        