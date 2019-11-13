class Solution:
    # def buddyStrings(self, A: str, B: str) -> bool:
    #     if len(A) != len(B):
    #         return False
    #     diff = []
    #     for a, b in zip(A,B):
    #         if a != b:
    #             diff.append((a,b))
    #     if len(diff) == 2 and diff[0] == (diff[-1][-1], diff[-1][0]):
    #         return True
    #     elif len(diff) == 0:
    #         for k, v in collections.Counter(A).items():
    #             if v >= 2:
    #                 return True
    #     return False
    
    
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]
