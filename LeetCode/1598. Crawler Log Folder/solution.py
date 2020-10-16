class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if step > 0:
                    step -= 1
            else:
                step += 1
        return step