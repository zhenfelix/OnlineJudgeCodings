class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = collections.defaultdict(int)
        res, left, n = 0, 0, len(s)
        for right in range(n):
            cnt[s[right]] += 1
            while left < n and sum(list(map(lambda x: x>0, cnt.values()))) == 3:
                res += n-right
                cnt[s[left]] -= 1
                left += 1
        return res
                
        
class Solution:
    # def numberOfSubstrings(self, s):
    #     res = i = 0
    #     count = {c: 0 for c in 'abc'}
    #     for j in range(len(s)):
    #         count[s[j]] += 1
    #         while all(count.values()):
    #             count[s[i]] -= 1
    #             i += 1
    #         res += i
    #     return res

    def numberOfSubstrings(self, s):
        res, last = 0, [-1] * 3
        for i, c in enumerate(s):
            last[ord(c) - 97] = i
            res += 1 + min(last)
        return res