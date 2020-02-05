class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        mp = {}
        for i, v in enumerate(sorted(list(set(arr)))):
            mp[v] = i+1
        return list(map(lambda x: mp[x], arr))