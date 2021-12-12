class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        pre, cnt = -2, 0
        for i, ch in enumerate(street):
            if ch == '.':
                continue
            if (i == 0 or street[i-1] == 'H') and (i == n-1 or street[i+1] == 'H'):
                return -1
            if pre == i-1:
                continue
            if i < n-1 and street[i+1] == '.':
                pre = i+1
            else:
                pre = i-1
            cnt += 1
        return cnt 


class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        ans = 0
        last = -2
        
        for i, ch in enumerate(street):
            if ch == 'H':
                if last == i - 1:
                    continue
                if i + 1 < n and street[i + 1] == '.':
                    last = i + 1
                    ans += 1
                elif i >= 1 and street[i - 1] == '.':
                    last = i - 1
                    ans += 1
                else:
                    return -1
                    
        return ans


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/jPIdc4/view/8u6s2V/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。