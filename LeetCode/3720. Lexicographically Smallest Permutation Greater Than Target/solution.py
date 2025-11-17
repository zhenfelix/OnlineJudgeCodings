class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        ct = [0] * 26
        for char in s:
            ct[ord(char) - ord('a')] += 1
        
        res = ""
        pref = []
        
        for i in range(n):
            t_ord = ord(target[i]) - ord('a')
            
            for j in range(t_ord + 1, 26):
                if ct[j] > 0:
                    ct[j] -= 1
                    
                    suf = []
                    for k in range(26):
                        suf.append(chr(k + ord('a')) * ct[k])
                    
                    cand = "".join(pref) + chr(j + ord('a')) + "".join(suf)
                    
                    res = cand
                        
                    ct[j] += 1
                    break
            
            if ct[t_ord] > 0:
                ct[t_ord] -= 1
                pref.append(target[i])
            else:
                break
        
        return res