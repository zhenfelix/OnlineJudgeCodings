class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 != 0:
            return []
        cc = Counter(changed)
        arr = []
        changed.sort()
        for x in changed:
            if cc[x] > 0:
                cc[x] -= 1
                cc[x*2] -= 1
                if cc[x*2] < 0:
                    return []
                arr.append(x)
        return arr 