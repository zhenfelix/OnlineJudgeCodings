class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (x[0],-x[1]))
        mx, res = 0, 0
        for _, h in properties[::-1]:
            res += h < mx
            mx = max(mx,h)
        return res


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        mx, res = 0, 0
        for _, h in sorted(properties, key = lambda x : (-x[0],x[1])):
            res += h < mx
            mx = max(mx,h)
        return res