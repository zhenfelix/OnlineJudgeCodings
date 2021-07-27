class Solution:
    def getLucky(self, s: str, k: int) -> int:
        snum = ''.join(map(lambda x: str(ord(x) - ord('a') + 1), s))
        for _ in range(k):
            snum = str(sum(map(int, snum)))
        return int(snum)


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/zesmlZ/view/SqRxlN/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# class Solution:
#     def getLucky(self, s: str, k: int) -> int:
#         def func(arr):
#             sums = 0
#             for ch in arr:
#                 sums += ord(ch)-ord('0')
#             return sums

#         cur = ''.join(str(ord(ch)-ord('a')+1) for ch in s)
#         for _ in range(k):
#             cur = str(cur)
#             cur = func(cur)
#         return cur
