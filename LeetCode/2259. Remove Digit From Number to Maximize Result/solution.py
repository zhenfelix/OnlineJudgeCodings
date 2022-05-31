class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = "0"
        for i, ch in enumerate(number):
            if ch == digit and int(number[:i]+number[i+1:]) > int(ans):
                ans = number[:i]+number[i+1:]
        return ans

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = "0"
        for i, ch in enumerate(number):
            if ch == digit and number[:i]+number[i+1:] > ans:
                ans = number[:i]+number[i+1:]
        return ans