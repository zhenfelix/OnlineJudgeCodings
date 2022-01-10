class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cc = Counter()
        cnt = 0
        for w in words:
            rw = w[1]+w[0]
            if cc[rw] > 0:
                cc[rw] -= 1
                cnt += 4
            else:
                cc[w] += 1
        for k, v in cc.items():
            if v > 0 and k[0] == k[1]:
                return cnt+2
        return cnt 