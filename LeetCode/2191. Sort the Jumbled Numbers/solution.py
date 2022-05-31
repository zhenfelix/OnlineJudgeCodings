class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        def func(x):
            base = 1
            y = 0
            if x == 0:
                return mapping[x]
            while x:
                y += mapping[x%10]*base
                base *= 10
                x //= 10
            return y 

        arr = []
        for i, x in enumerate(nums):
            arr.append((func(nums[i]),i))
        arr.sort()
        return [nums[i] for x, i in arr]

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda num: int(''.join(map(str, [mapping[int(x)] for x in str(num)]))))


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/9WhoB7/view/s15EHo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。