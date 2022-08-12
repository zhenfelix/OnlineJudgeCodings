class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cc = set()
        for ch in s:
            if ch in cc:
                return ch 
            cc.add(ch)
        return ""