class Solution:
    def largestInteger(self, num: int) -> int:
        es, os = [], []
        for i, ch in enumerate(list(str(num))):
            if int(ch)&1:
                os.append(ch)
            else:
                es.append(ch)
        os.sort()
        es.sort()
        ans = []
        # print(os,es)
        for ch in list(str(num)):
            if int(ch)&1:
                ans.append(os.pop())
            else:
                ans.append(es.pop())
        return int(''.join(ans))