class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {v: i for i, v in enumerate(arr)}
        n = len(arr)
        for row in pieces:
            if row[0] not in mp:
                return False
            i = mp[row[0]]
            for a in row:
                if i >= n or arr[i] != a:
                    return False
                arr[i] = 0 
                i += 1
        return True

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pos = {v: i for i, v in enumerate(arr)}
        for p in pieces:
            for i, v in enumerate(p):
                if v not in pos:
                    return False
                if i and pos[p[i]]-pos[p[i-1]] != 1:
                    return False
        return True

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