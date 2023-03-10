class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        cur = 0
        for ch in word:
            ch = int(ch)
            cur = (cur*10+ch)
            cur = cur%m 
            if cur == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans 