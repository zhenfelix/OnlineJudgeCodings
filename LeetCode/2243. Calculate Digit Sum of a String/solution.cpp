class Solution {
public:
    string digitSum(string s, int k) {
        while (s.size() > k) {
            string nxt;
            int sm = 0;
            for (int i = 0; i < s.size(); i++) {
                sm += s[i] - '0';
                if (i % k == k - 1 || i + 1 == s.size()) nxt += to_string(sm), sm = 0;
            }
            s = nxt;
        }
        return s;
    }
};


作者：TsReaper
链接：https://leetcode-cn.com/circle/discuss/XxY039/view/A9HquX/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。