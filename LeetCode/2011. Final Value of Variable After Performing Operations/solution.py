class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(('+' in s) - ('-' in s) for s in operations)


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            if '-' in op:
                res -= 1
            else:
                res += 1
        return res