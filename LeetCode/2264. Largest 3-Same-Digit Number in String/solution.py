class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            t = str(i) * 3
            if t in num:
                return t
        return ""


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/GL2IJv/view/hjOlWd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ""
        def judge(x):
            return x[0] == x[1] == x[2]
        for i in range(0,n-2):
            if judge(num[i:i+3]) and num[i:i+3] > ans:
                ans = num[i:i+3]
        return ans