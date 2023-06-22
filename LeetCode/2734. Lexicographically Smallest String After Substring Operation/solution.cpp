class Solution {
public:
    string smallestString(string s) {
        // 是否进行过操作
        bool flag = false;
        for (char &c : s) {
            if (c == 'a') {
                // 遇到 a 而且之前已经进行过一次操作了，结束
                if (flag) break;
            } else {
                // 将最前面一段不含 a 的连续子串进行变化
                flag = true;
                c--;
            }
        }
        // 全是 a，只能把最后一个字符变成 z
        if (!flag) s[s.size() - 1] = 'z';
        return s;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/bvOqiS/view/FomS8E/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。