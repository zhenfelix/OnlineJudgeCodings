class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        seen = set(nums)
        for a, b in zip(moveFrom,moveTo):
            if a in seen:
                seen.remove(a)
                seen.add(b)
        return sorted(list(seen))

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        cnt = set(nums)
        for f, t in zip(moveFrom, moveTo):
            cnt.remove(f)
            cnt.add(t)
        return sorted(cnt)


作者：endlesscheng
链接：https://leetcode.cn/problems/relocate-marbles/solution/jian-ji-xie-fa-by-endlesscheng-thul/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。