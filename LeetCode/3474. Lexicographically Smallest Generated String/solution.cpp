class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.size(), m = str2.size();
        string ans;
        ans.resize(n + m - 1);

        // flag[i] 表示下标 i 能否修改
        bool flag[n + m - 1];
        memset(flag, 0, sizeof(flag));
        // 先满足所有 T 的要求
        for (int i = 0; i < n; i++) if (str1[i] == 'T')
            for (int j = 0; j < m; j++) ans[i + j] = str2[j], flag[i + j] = true;
        // 检查一遍子串之间的覆盖没有影响答案
        for (int i = 0; i < n; i++) if (str1[i] == 'T')
            if (ans.substr(i, m) != str2) return "";
        
        // 把没填的位置都填上 a
        for (char &c : ans) if (c == 0) c = 'a';    

        // 接下来满足 F 的要求
        for (int i = 0; i < n; i++) if (str1[i] == 'F' && ans.substr(i, m) == str2) {
            bool failed = true;
            // 找到最后一个能改的位置，改成 b
            for (int j = m - 1; j >= 0; j--) if (!flag[i + j]) { ans[i + j] = 'b'; failed = false; break; }
            // 找不到就无解
            if (failed) return "";
        }
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/lexicographically-smallest-generated-string/solutions/3591754/gou-zao-tan-xin-by-tsreaper-4gtj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。