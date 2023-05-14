class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        def check(pre):
            cur = pre
            for a in derived:
                cur ^= a  
            return cur == pre 
        return check(0) or check(1)