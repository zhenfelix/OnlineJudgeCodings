class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for v, w in items1:
            mp[v] += w 
        for v, w in items2:
            mp[v] += w 
        ans = sorted([[k, v] for k, v in mp.items()])
        return ans