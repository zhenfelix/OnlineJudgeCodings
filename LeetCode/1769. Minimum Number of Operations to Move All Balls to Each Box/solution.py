class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n
        sums, cnt = 0, 0
        for i in range(n):
            ans[i] += sums
            if boxes[i] == '1':
                cnt += 1
            sums += cnt
        sums, cnt = 0, 0
        for i in range(n)[::-1]:
            ans[i] += sums
            if boxes[i] == '1':
                cnt += 1
            sums += cnt
        return ans 