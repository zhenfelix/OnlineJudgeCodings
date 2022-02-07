class Solution:
    def smallestNumber(self, num: int) -> int:
        neg = False
        if num == 0:
            return 0
        if num < 0:
            num = -num
            neg = True
        cc = Counter(str(num))
        res = []
        if neg:
            for i in range(10)[::-1]:
                ch = str(i)
                res += [ch]*cc[ch]
            return -int(''.join(res))
        else:
            for i in range(1,10):
                ch = str(i)
                if cc[ch] > 0:
                    cc[ch] -= 1
                    res.append(ch)
                    break
            for i in range(10):
                ch = str(i)
                res += [ch]*cc[ch]
            return int(''.join(res))

