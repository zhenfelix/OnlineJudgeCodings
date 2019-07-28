class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        mp = {}
        A = sorted(A, reverse = True)
        for a in A:
            if a in mp:
                mp[a] += 1
            else:
                mp[a] = 1
        for a in A:
            if mp[a] == 1:
                return a
        return -1
        
            