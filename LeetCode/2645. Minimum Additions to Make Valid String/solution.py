class Solution:
    def addMinimum(self, word: str) -> int:
        return (sum(a >= b for a, b in zip(word, word[1:])) + 1) * 3 - len(word)


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/YQDX7V/view/lUNYmJ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def addMinimum(self, word: str) -> int:
        word += 'a'
        ans = 0
        cnt = 1
        n = len(word)
        for i in range(1,n):
            if word[i] <= word[i-1]:
                ans += 3-cnt
                cnt = 1
            else:
                cnt += 1
        return ans 