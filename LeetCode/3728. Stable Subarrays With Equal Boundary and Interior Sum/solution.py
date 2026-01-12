class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        ans = s = 0
        cc = Counter()
        for i in range(n-1):
            s += capacity[i]
            ans += cc[s,capacity[i+1]]
            cc[s+capacity[i],capacity[i]] += 1
        return ans 