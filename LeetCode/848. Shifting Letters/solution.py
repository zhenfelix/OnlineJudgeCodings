class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        arr = [ord(ch)-ord('a') for ch in S]
        n, cur = len(S), 0
        for i in range(n-1,-1,-1):
            cur += shifts[i]
            cur %= 26
            arr[i] += cur
            arr[i] %= 26
        return ''.join(map(lambda x: chr(ord('a')+x), arr))