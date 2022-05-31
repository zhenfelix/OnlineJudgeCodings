class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp = dict()
        ans = float('inf')
        for i, x in enumerate(cards):
            if x in mp:
                ans = min(ans, i-mp[x])
            mp[x] = i 
        return -1 if ans == float('inf') else ans+1