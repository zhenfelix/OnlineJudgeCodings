class Solution:
    def countVowels(self, word: str) -> int:        
        n = len(word)
        return sum((i + 1) * (n - i) for i, ch in enumerate(word) if ch in 'aeiou')


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/JXlHA8/view/dDXpJp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。