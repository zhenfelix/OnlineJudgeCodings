class Solution:
    def largestPalindromic(self, num: str) -> str:
        res = []
        cc = Counter(num)
        flag = ''
        for i in range(10)[::-1]:
            ch = str(i)
            if ch == '0' and not res:
                continue
            if cc[ch] > 0:
                if cc[ch] > 1:
                    res.append(ch*(cc[ch]//2))
                if not flag and (cc[ch]&1):
                    flag = ch 
            # print(res)
        return ''.join(res+[flag]+res[::-1]) or '0'