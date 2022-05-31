class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a, b, cnt = 0, 0, 0
        x, y = pattern[0], pattern[1]
        for ch in text:
            if ch == x:
                a += 1
            elif ch == y:
                cnt += a
                b += 1
        if x == y:
            cnt = a+b+1
            return cnt*(cnt-1)//2
        return cnt + max(a,b)

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        if pattern[0] == pattern[1]:
            cnt = Counter(text)[pattern[0]]
            cnt += 1
            return cnt*(cnt-1)//2
        res = 0
        cnt = 1
        cur = 0
        for ch in text:
            if ch == pattern[0]:
                cnt += 1
            elif ch == pattern[1]:
                cur += cnt
        res = max(res, cur)
        cnt, cur = 1, 0
        for ch in text[::-1]:
            if ch == pattern[1]:
                cnt += 1
            elif ch == pattern[0]:
                cur += cnt
        res = max(res, cur)
        return res


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # if pattern[0] == pattern[1]:
        #     cnt = Counter(text)[pattern[0]]
        #     cnt += 1
        #     return cnt*(cnt-1)//2
        res = 0
        cnt = 1
        cur = 0
        for ch in text:
            if ch == pattern[1]:
                cur += cnt
            if ch == pattern[0]:
                cnt += 1
                
        res = max(res, cur)
        cnt, cur = 1, 0
        for ch in text[::-1]:
            if ch == pattern[0]:
                cur += cnt
            if ch == pattern[1]:
                cnt += 1
        res = max(res, cur)
        return res
