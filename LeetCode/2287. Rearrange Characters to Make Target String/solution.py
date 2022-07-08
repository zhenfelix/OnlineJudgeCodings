class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cc1, cc2 = Counter(s), Counter(target)
        res = float('inf')
        for k, v in cc2.items():
            res = min(res, cc1[k]//v)
        return res