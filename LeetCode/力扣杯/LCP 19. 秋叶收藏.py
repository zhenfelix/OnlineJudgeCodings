class Solution:
    def minimumOperations(self, leaves: str) -> int:
        def diff(s1, s2):
            cnt = 0
            for i, ch in enumerate(s1):
                if s1[i] != s2[i]:
                    cnt += 1
            return cnt

        rrr, rry, ryr = diff(leaves[:3],'rrr'), min(diff(leaves[:3],'rry'),diff(leaves[:3],'ryy')), diff(leaves[:3],'ryr')
        for ch in leaves[3:]:
            rrr, rry, ryr = rrr + (ch != 'r'), min(rrr + (ch != 'y'), rry + (ch != 'y')), min(rry + (ch != 'r'), ryr + (ch != 'r'))
        return ryr 
