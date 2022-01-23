class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        res = 0
        def check(s):
            for i in range(n):
                if (s>>i)&1 == 1:
                    for j in range(n):
                        if statements[i][j] == 2:
                            continue
                        if statements[i][j] != ((s>>j)&1):
                            return False
            return True

        for s in range(1<<n):
            if check(s):
                res = max(res, sum(((s>>i)&1)==1 for i in range(n)))
        return res
