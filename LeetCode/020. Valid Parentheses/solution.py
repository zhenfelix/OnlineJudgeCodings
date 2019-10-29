class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mp = {'(':-1,'{':-2,'[':-3,']':3,'}':2,')':1}
        st = []
        for ch in s:
            if mp[ch] < 0:
                st.append(mp[ch])
            elif st and st[-1]+mp[ch] == 0:
                st.pop()
            else:
                return False
        return st == []