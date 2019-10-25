from collections import Counter

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        return self.lengthOfLongestSubstringKDistinct(s,2)
        
        
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        left = right = 0
        cnt = 0
        n = len(s)
        cc = Counter()
        while left < n and right < n:
            while right < n:
                ch = s[right]
                if cc[ch] == 0:
                    cnt += 1
                if cnt > k:
                    cnt -= 1
                    break
                cc[ch] += 1
                right += 1
            # print(left,right,cnt)
            res = max(res,right-left)
            ch = s[left]
            cc[ch] -= 1
            if cc[ch] == 0:
                cnt -= 1
            left += 1
        return res