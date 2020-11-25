class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        s1, s2 = set(arr), set(reduce(lambda x,y: x+y, pieces, []))
        if s1 != s2:
            return False
        mp = {}
        for i, a in enumerate(arr):
            mp[a] = i 
        for piece in pieces:
            for i, a in enumerate(piece):
                if i:
                    # if mp[piece[i]] < mp[piece[i-1]]:
                    if mp[piece[i]] != mp[piece[i-1]] + 1:
                        return False 
        return True