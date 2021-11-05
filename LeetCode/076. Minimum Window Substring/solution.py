class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = set(t)
        cc = Counter(t)
        cnt = len(cc)
        res = [float('inf'), -1]
        left = 0
        for right, ch in enumerate(s):
            if ch in seen:
                cc[ch] -= 1
                if cc[ch] == 0:
                    cnt -= 1
            while cnt == 0:
                if right-left+1 < res[0]:
                    res = [right-left+1,right]
                ch = s[left]
                if ch in seen:
                    if cc[ch] == 0:
                        cnt += 1
                    cc[ch] += 1
                left += 1
        return "" if res[0] == float('inf') else s[res[-1]-res[0]+1:res[-1]+1]



from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, length = "", float("inf")
        sc, tc = Counter(), Counter(t)
        left, cnt = 0, len(tc)
        for right, ch in enumerate(s):
            sc[ch] += 1
            if ch in tc and sc[ch] == tc[ch]:
                cnt -= 1
            while cnt == 0:
                if right-left+1 < length:
                    length = right-left+1
                    res = s[left:right+1]
                sc[s[left]] -= 1
                if sc[s[left]] < tc[s[left]]:
                    cnt += 1
                left += 1
        return res
            