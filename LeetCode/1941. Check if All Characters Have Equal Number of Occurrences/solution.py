# class Solution:
#     def areOccurrencesEqual(self, s: str) -> bool:
#         cc = Counter(s)
#         arr = [k for k, v in cc.items()]
#         if all(cc[a] == cc[b] for a,b in zip(arr,arr[1:])):
#             return True
#         return False



# class Solution:
#     def areOccurrencesEqual(self, s: str) -> bool:
#         cc = Counter(s)
#         vals = [v for v in cc.values()]
#         if all(v == vals[-1] for v in vals):
#             return True
#         return False

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1