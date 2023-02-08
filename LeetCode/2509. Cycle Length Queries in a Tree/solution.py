class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for a, b in queries:
            ans.append(1)
            while a != b:
                if a > b:
                    a //= 2
                    ans[-1] += 1
                else:
                    b //= 2
                    ans[-1] += 1
        return ans