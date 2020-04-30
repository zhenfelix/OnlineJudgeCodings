class Solution:
    def maxScore(self, s: str) -> int:
        zeros = ones = 0
        ans = float("-inf")
        
        for ch in s[:-1]:
            if ch == "0": zeros += 1
            else: ones -= 1
            ans = max(ans, zeros + ones)
        
        return ans - ones + (1 if s[-1] == "1" else 0)

# class Solution:
#     def maxScore(self, s: str) -> int:
#         n = len(s)
#         return max(sum(ch=='0' for ch in s[:k])+sum(ch=='1' for ch in s[k:]) for k in range(1,n))
#         