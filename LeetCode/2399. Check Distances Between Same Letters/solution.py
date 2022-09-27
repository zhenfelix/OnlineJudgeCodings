class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        pos = dict()
        for i, ch in enumerate(s):
            if ch in pos:
                if distance[ord(ch)-ord('a')] != i-pos[ch]-1:
                    return False
            else:
                pos[ch] = i
        return True