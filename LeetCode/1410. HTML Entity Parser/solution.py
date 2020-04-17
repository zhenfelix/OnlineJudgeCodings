class Solution:
    def entityParser(self, text: str) -> str:
        res, mark = "", ""
        mp = {"&quot;":"\"","&apos;":"\'","&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
        for ch in text:
            if mark:
                if ch == '&':
                    res += mark
                    mark = ch
                elif ch == ';':
                    mark += ch
                    if mark in mp:
                        res += mp[mark]
                    else:
                        res += mark
                    mark = ''
                else:
                    mark += ch
            else:
                if ch == '&':
                    mark += ch
                else:
                    res += ch
        return res
                    
        