class Solution:
    def smallestGoodBase(self, n: str) -> str:
        target, sz = int(n), len(bin(int(n)))-2
        # print(target,sz)
        
        def search(cnt):
            left, right = 1, target
            # print(left,right,cnt)
            while left <= right:
                base = (left + right)//2
                cur, sums = 1, 0
                for _ in range(cnt):
                    sums += cur
                    cur *= base 
                    if sums > target:
                        break
                # print(left,right,cnt,base,sums)
                if sums == target:
                    return str(base)
                elif sums > target:
                    right = base - 1
                else:
                    left = base + 1
            return ''

        for d in range(2,sz+1)[::-1]:
            res = search(d)
            if res:
                return res
        return ''