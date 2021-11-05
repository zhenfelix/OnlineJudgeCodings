import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        return len(list(filter(lambda x: re.match('[a-z]*([a-z]-[a-z])?[a-z]*[!\.,]?$', x), sentence.split())))


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/NZT0w3/view/dlGnz5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        cnt = 0
        for word in words:
            if any(ch.isdigit() for ch in word):
                continue
            if word.count('-') > 1 or word[0] == '-' or word[-1] == '-':
                continue
            # print(word)
            if word.count('-') == 1:
                a, b = word.split('-')
                if not a or not b:
                    continue
                if not a[-1].isalpha() or not b[0].isalpha():
                    continue
            if any(ch in ",.!" for ch in word[:-1]):
                continue
            cnt += 1
        return cnt