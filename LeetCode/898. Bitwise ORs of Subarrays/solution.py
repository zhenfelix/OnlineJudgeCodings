class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        seen, prefix = set(), set()
        for a in A:
            tmp = {p|a for p in prefix}
            tmp.add(a)
            prefix = tmp
            seen |= prefix
        return len(seen)