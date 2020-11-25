class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        p = suma = 0
        for ai, mi in tasks:
            p = max(p, suma + mi)
            suma += ai
        return p


# 作者：zerotrac2
# 链接：https://leetcode-cn.com/problems/minimum-initial-energy-to-finish-tasks/solution/wan-cheng-suo-you-ren-wu-de-zui-shao-chu-shi-neng-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。