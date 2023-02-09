class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        mx = Counter()
        for s in demand:
            mx |= Counter(s)
        return sum(mx.values())


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        seen = Counter()
        for s in demand:
            tmp = seen.copy()
            for ch in s:
                if tmp[ch] == 0:
                    seen[ch] += 1
                else:
                    tmp[ch] -= 1
        return sum(v for k, v in seen.items())
