class Solution:
    def digitCount(self, num: str) -> bool:
        cc = Counter(num)
        return all(cc[str(i)] == int(x) for i, x in enumerate(num)