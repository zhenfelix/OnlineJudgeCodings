class Solution(object):
    def maximumNumberOfOnes(self, C, R, K, maxOnes):
        # every K*K square has at most maxOnes ones
        count = [0] * (K*K)
        for r in range(R):
            for c in range(C):
                code = (r%K) * K + c%K
                count[code] += 1
        count.sort()
        ans = 0
        for _ in range(maxOnes):
            ans += count.pop()
        return ans