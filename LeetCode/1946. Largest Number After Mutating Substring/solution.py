class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res = [int(ch) for ch in num]
        mutation = False
        for i, x in enumerate(res):
            if mutation and change[x] < x:
                break
            if change[x] > x:
                res[i] = change[x]
                mutation = True
        return ''.join(str(ch) for ch in res)