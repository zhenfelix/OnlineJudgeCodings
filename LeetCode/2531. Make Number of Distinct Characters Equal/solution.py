import string  

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cc1, cc2 = Counter(word1), Counter(word2)
        sz1, sz2 = len(set(word1)), len(set(word2))
        for ch1 in string.ascii_lowercase:
            if cc1[ch1] == 0: continue
            cc1[ch1] -= 1 
            if cc1[ch1] == 0: sz1 -= 1
            for ch2 in string.ascii_lowercase:
                if cc2[ch2] == 0: continue
                cc2[ch2] -= 1
                if cc2[ch2] == 0: sz2 -= 1
                if cc2[ch1] == 0: sz2 += 1 
                if cc1[ch2] == 0: sz1 += 1
                if sz1 == sz2: return True
                if cc2[ch1] == 0: sz2 -= 1 
                if cc1[ch2] == 0: sz1 -= 1
                if cc2[ch2] == 0: sz2 += 1
                cc2[ch2] += 1
                
            if cc1[ch1] == 0: sz1 += 1
            cc1[ch1] += 1
        return False
                 

