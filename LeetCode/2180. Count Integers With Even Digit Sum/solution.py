class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num + 1):
            if sum(map(int, str(i))) % 2 == 0:
                ans += 1
        return ans


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/76BnS1/view/QLHc5J/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def countEven(self, num: int) -> int:
        def calc(x):
            v = 0
            while x:
                v += x%10
                x //= 10
            return v%2 == 0 

        return sum(calc(i) for i in range(1,num+1))