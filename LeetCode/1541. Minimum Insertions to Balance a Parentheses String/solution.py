class Solution:
    def minInsertions(self, s: str) -> int:
        s = s+'#'
        cnt, left, right = 0, 0, 0
        for ch in s:
            if ch == '(' or ch == '#':
                if right > 0 or ch == '#':
                    cnt += (right&1)
                    left -= (right+1)//2
                    if left < 0:
                        cnt -= left
                        left = 0
                    right = 0
                    if ch == '#':
                        cnt += left*2
                left += 1
            else:
                right += 1
            # print(ch,left,right,cnt)
        return cnt