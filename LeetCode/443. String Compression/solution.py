class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt, pos = 0, 0
        n = len(chars)
        for i in range(n):
            cnt += 1
            if i == n-1 or chars[i] != chars[i+1]:
                chars[pos] = chars[i]
                pos += 1
                tmp = str(cnt)
                cnt = 0
                # print(chars[i],tmp)
                if tmp == '1':
                    continue
                for x in tmp:
                    chars[pos] = x
                    pos += 1
                
        return pos


