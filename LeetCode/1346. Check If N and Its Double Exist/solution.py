class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cc = Counter(arr)
        for a in arr:
            if cc[a*2] + (a != 0) > 1:
            # if (a == 0 and cc[0] > 1) or (a != 0 and cc[a*2] > 0):
                return True
        return False