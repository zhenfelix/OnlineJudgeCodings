class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        st = []  # 栈中保存 [字符, 连续出现次数]
        for b in s:
            if st and st[-1][0] == b:
                st[-1][1] += 1  # 连续相同括号个数 +1
            else:
                st.append([b, 1])  # 新的括号

            # 栈顶的 k 个右括号与栈顶下面的 k 个左括号抵消
            if b == ')' and len(st) > 1 and st[-1][1] == k and st[-2][1] >= k:
                st.pop()
                st[-1][1] -= k
                if st[-1][1] == 0:
                    st.pop()

        return ''.join(b * cnt for b, cnt in st)

作者：灵茶山艾府
链接：https://leetcode.cn/problems/remove-k-balanced-substrings/solutions/3798502/lin-xiang-xiao-chu-wen-ti-de-tao-lu-zhan-kb1j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。