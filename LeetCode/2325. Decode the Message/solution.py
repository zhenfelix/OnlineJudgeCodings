class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        message = list(message)
        cur = 'a'
        mp = dict()
        for ch in key:
            if ch == ' ':
                continue
            if ch not in mp:
                mp[ch] = cur
                cur = chr(ord(cur)+1)
        return ''.join([mp[ch] if ch != ' ' else ch for ch in message])