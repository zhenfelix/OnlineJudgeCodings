class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        tmp = blocks[:k].count('W')
        ans = tmp
        for i in range(len(blocks) - k):
            tmp += - (blocks[i] == 'W') + (blocks[i + k] == 'W')
            ans = min(ans, tmp)
        return ans


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/oZvJdG/view/7BqGw6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        n = len(blocks)
        cnt = 0
        for right in range(n):
            if blocks[right] == 'W':
                cnt += 1
            if right >= k:
                if blocks[right-k] == 'W':
                    cnt -= 1
            if right >= k-1:
                ans = min(ans, cnt)
        return ans 