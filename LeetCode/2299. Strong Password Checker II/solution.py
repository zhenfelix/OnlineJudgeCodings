class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special = "!@#$%^&*()-+"
        alpha = ''.join(chr(ord('a')+ch) for ch in range(26))
        Alpha = ''.join(chr(ord('A')+ch) for ch in range(26))

        if len(password) < 8:
            return False
        if not any(ch in alpha for ch in password):
            return False
        if not any(ch in Alpha for ch in password):
            return False
        if not any(ch.isdigit() for ch in password):
            return False
        if not any(ch in special for ch in password):
            return False
        if any(a == b for a, b in zip(password[:-1],password[1:])):
            return False
        return True


class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        if len(s) < 8:
            return False
        for i in s:
            if i.isdigit():
                break
        else:
            return False
        for i in s:
            if i.islower():
                break
        else:
            return False
        for i in s:
            if i.isupper():
                break
        else:
            return False
        for i in s:
            if i in "!@#$%^&*()-+":
                break
        else:
            return False
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                return False
        return True


作者：caidd
链接：https://leetcode.cn/circle/discuss/zEDpCN/view/0TsH9Q/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。