class Solution:
    def minSwaps(self, s):
        bal, ans = 0, 0
        for symb in s:
            if symb == "[": bal += 1
            else: bal -= 1
            ans = min(bal, ans)
        return (-ans + 1)//2


class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        left, right = 0, n-1
        Open, Close = 0, 0
        cnt = 0
        while left < right:
            while left < right and Open >= 0:
                if s[left] == '[':
                    Open += 1
                else:
                    Open -= 1
                if Open >= 0:
                    left += 1
            while left < right and Close >= 0:
                if s[right] == ']':
                    Close += 1
                else:
                    Close -= 1
                if Close >= 0:
                    right -= 1

            if left < right:
                cnt += 1
                Open, Close = 1, 1
                left += 1
                right -= 1
        return cnt