# class Solution:
#     def countConsistentStrings(self, allowed, words):
#         return sum(all(c in allowed for c in w) for w in words)        

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(list(allowed))
        res = 0
        for word in words:
            cur = set(list(word))
            if cur == (cur&allowed):
                res += 1
        return res 