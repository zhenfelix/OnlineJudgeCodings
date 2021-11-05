class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = list(map(int, filter(lambda x: x.isnumeric(), s.split())))
        return all([pre < nxt for pre, nxt in zip(nums[:-1], nums[1:])])


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/89Uy1V/view/7QeRXQ/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。