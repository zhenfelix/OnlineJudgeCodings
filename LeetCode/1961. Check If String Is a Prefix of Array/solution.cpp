class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        int n = s.size();
        int ptr = 0;
        for (string &word : words) {
            int m = word.size();
            int i = 0;
            while (i < m && ptr < n && word[i] == s[ptr])
                i++, ptr++;
            if (i == m && ptr == n)
                return true;
            if (i != m)
                return false;
        }
        return false;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/avaR15/view/EIciXR/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。