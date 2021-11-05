class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        sums, left, res = 0, 0, 0
        n = len(answerKey)
        for right in range(n):
            if answerKey[right] == 'T':
                sums += 1
            while sums > k:
                if answerKey[left] == 'T':
                    sums -= 1
                left += 1
            res = max(res, right-left+1)
        sums, left = 0, 0
        for right in range(n):
            if answerKey[right] == 'F':
                sums += 1
            while sums > k:
                if answerKey[left] == 'F':
                    sums -= 1
                left += 1
            res = max(res, right-left+1)
        return res

