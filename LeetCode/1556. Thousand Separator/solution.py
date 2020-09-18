class Solution:
    def thousandSeparator(self, n: int) -> str:
        arr = deque(list(str(n)))
        res = []
        while arr:
            cur = arr.popleft()
            res.append(cur)
            if len(arr) > 0 and len(arr)%3 == 0:
                res.append('.')
        return ''.join(res)