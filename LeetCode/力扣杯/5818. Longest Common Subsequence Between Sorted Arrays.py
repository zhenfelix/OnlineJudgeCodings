class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        cc = Counter()
        for arr in arrays:
            for a in arr:
                cc[a] += 1
        res = [i for i in range(1,101) if cc[i] == n]
        return res 