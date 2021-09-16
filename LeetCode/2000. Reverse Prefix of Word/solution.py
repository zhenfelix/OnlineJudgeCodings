# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         idx = word.find(ch)
#         if idx == -1:
#             return word
#         word = list(word)
#         return ''.join(word[:idx+1][::-1]+word[idx+1:])


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        return word if i == -1 else word[:i + 1][::-1] + word[i + 1:]


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/qfdpX8/view/MZB6bJ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。