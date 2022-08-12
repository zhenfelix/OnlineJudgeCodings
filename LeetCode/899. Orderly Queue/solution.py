class Solution:
    def orderlyQueue(self, S, K):
        return "".join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        if k == 1:
            s += s 
            return min(s[i:i+n] for i in range(n))
        return ''.join(sorted(list(s)))    