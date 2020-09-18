class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank, mp = {}, {}
        for i, preference in enumerate(preferences):
            for r, p in enumerate(preference):
                rank[i,p] = r 
        for a, b in pairs:
            mp[a] = b
            mp[b] = a
        cnt = 0
        for i, preference in enumerate(preferences):
            for r, p in enumerate(preference):
                if r < rank[i,mp[i]] and rank[p,i] < rank[p,mp[p]]:
                    cnt += 1
                    break
        return cnt