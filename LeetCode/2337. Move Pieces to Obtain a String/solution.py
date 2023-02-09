class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def convert(s):
            ans = []
            for ch in s:
                if ch != '_':
                    ans.append(ch)
            return ''.join(ans)
        if convert(start) != convert(target):
            return False
        n = len(start)
        # print(n)
        j = 0
        for i, ch in enumerate(target):
            if ch == '_':
                continue
            while start[j] != ch:
                j += 1  
            if ch == 'L':
                if j < i:
                    # print(i,j,'L',start[j])
                    return False 
            else:
                if j > i:
                    # print(i,j,'R',start[j])
                    return False
            j += 1
        return True

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        v1, v2 = [], []
        for i in range(n):
            if start[i] != '_':
                v1.append((start[i],i))
            if target[i] != '_':
                v2.append((target[i],i))
        if len(v1) != len(v2):
            return False
        for (ch1,i),(ch2,j) in zip(v1,v2):
            if ch1 != ch2:
                return False
            if ch1 == 'L':
                if i < j:
                    return False
            else:
                if i > j:
                    return False
        return True




class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        cc, cc2 = Counter(start), Counter(target)
        if cc['_'] != cc2['_'] or cc['L'] != cc2['L'] or cc['R'] != cc2['R']:
            return False
        cnt = 0
        for i in range(n):
            if target[i] == 'L':
                cnt += 1
            if target[i] == 'R' or start[i] == 'R':
                cnt = 0
            if start[i] == 'L':
                cnt -= 1
                if cnt < 0:
                    return False
        if cnt != 0:
            return False
        cnt = 0
        for i in range(n)[::-1]:
            if target[i] == 'R':
                cnt += 1
            if target[i] == 'L' or start[i] == 'L':
                cnt = 0
            if start[i] == 'R':
                cnt -= 1
                if cnt < 0:
                    return False
        if cnt != 0:
            return False
        return True

