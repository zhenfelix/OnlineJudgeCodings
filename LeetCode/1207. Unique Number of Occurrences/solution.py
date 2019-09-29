from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cc = Counter(arr)
        ex = set()
        for k, v in cc.items():
            if v in ex:
                return False
            ex.add(v)
        return True