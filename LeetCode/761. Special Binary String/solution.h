class Solution {
public:
    string makeLargestSpecial(string_view s) {
        const int n = s.size();
        if (n == 0) return "";
        int stk = 0, pos = 0;
        vector<string> children;
        for (int i = 0;i < n;++i) {
            switch (s[i]) {
            case '1':
                // 栈中增加一个左括号
                // 增加前栈为空说明当前是一个新的极小括号序列的开头
                // 将新的极小括号序列的开始位置记录下来
                if (stk++ == 0)
                    pos = i;
                break;
            case '0':
                // 栈中减少一个左括号
                // 减少后栈为空说明当前已经找到了一个完整的极小括号序列
                // 将极小括号序列去除最外围的括号后，递归计算最大值
                // 将递归得到的子括号序列加入列表
                if (--stk == 0)
                    children.push_back("1" + makeLargestSpecial(s.substr(pos + 1, i - pos - 1)) + "0");
                break;
            }
        }
        // 将子括号序列按从大到小排序
        sort(children.begin(), children.end(), greater<string>{});
        return reduce(children.begin(), children.end(), ""s);
    }
};


作者：vclip
链接：https://leetcode.cn/problems/special-binary-string/solution/onlogn-by-vclip-eyy8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。