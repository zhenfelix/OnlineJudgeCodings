class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = inf 
        n = len(words)
        for i in range(n):
            if words[(startIndex+i)%n] == target:
                ans = min(ans,i)
            if words[(startIndex-i+n)%n] == target:
                ans = min(ans,i)
        return -1 if ans == inf else ans 