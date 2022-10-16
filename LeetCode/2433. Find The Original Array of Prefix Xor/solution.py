class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = []
        pref.append(0)
        for i in range(n):
            arr.append(pref[i]^pref[i-1])
        return arr