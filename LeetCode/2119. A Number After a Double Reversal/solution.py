class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/NS4Y2j/view/dIMeD8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        return num == int(str(int(s[::-1]))[::-1])