class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        arr = list(num)
        while arr and arr[-1] == '0':
            arr.pop()
        return ''.join(arr)