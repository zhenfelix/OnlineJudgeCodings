class Solution:
    def isDecomposable(self, s: str) -> bool:
        # if len(s) < 5:
        #     return False
        s += '$'
        flag = False
        cnt = 1
        for a, b in zip(s,s[1:]):
            if a == b:
                cnt += 1
            else:
                if cnt%3 == 2:
                    if flag:
                        return False
                    else:
                        flag = True
                elif cnt%3 != 0:
                    return False
                cnt = 1
        return flag

