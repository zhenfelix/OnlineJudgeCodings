class Solution:
    def minTimeToType(self, word: str) -> int:
        cnt = 0
        cur = 'a'
        for ch in word:
            move = max(ord(ch)-ord(cur), ord(cur)-ord(ch))
            # print(move)
            cnt += min(move, 26-move)
            cur = ch 
        return cnt+len(word)

class Solution:
    def minTimeToType(self, word: str) -> int:
        cnt = 0
        cur = 'a'
        for ch in word:
            move = (ord(ch)-ord(cur)+26)%26
            # print(move)
            cnt += min(move, 26-move)
            cur = ch 
        return cnt+len(word)