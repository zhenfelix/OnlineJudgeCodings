class Solution {
public:
    string finalString(string s) {
        string ans;
        for (char c : s) {
            if (c == 'i') reverse(ans.begin(), ans.end());
            else ans.push_back(c);
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/chtVBq/view/Bd2wEn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    string finalString(string s) {
        // 用双端队列维护答案
        deque<char> q;
        // flag == true 表示现在是反转的字符串
        bool flag = false;
        for (char c : s) {
            if (c == 'i') flag = !flag;
            else {
                // 字符串反转了，字符加在答案左边
                if (flag) q.push_front(c);
                // 字符串没有反转，字符加在答案右边
                else q.push_back(c);
            }
        }
        
        string ans;
        for (char c : q) ans.push_back(c);
        // 看是否要反转输出答案
        if (flag) reverse(ans.begin(), ans.end());
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/chtVBq/view/Bd2wEn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。