class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s1, e1 = event1
        s2, e2 = event2
        return s1 <= e2 and s2 <= e1


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s1, e1 = event1
        s2, e2 = event2
        if s1 <= e2 and s2 <= e1:
            return True 
        return False