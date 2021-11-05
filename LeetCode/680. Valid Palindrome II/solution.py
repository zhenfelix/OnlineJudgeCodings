class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right, cnt):
            if left >= right:
                return True
            if s[left] == s[right]:
                return check(left+1, right-1, cnt)
            if cnt > 0:
                return check(left+1, right, cnt-1) or check(left, right-1, cnt-1)
            return False
        return check(0, len(s)-1, 1)