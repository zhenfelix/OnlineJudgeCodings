class Solution {
public:
    string smallestBeautifulString(string s, int k) {
        int n = s.size();
        
        // 这个函数从 s[n - 1] 开始尝试修改，返回最少要修改到哪个位置 + 1
        auto gao = [&]() {
            for (int i = n - 1; i >= 0; i--) {
                // 枚举比 s[i] 大，且是字母表前 k 个的字符
                for (int j = s[i] + 1; j < k + 'a'; j++) {
                    // 当前字符和前两个字符中的某一个相同，不行
                    if ((i >= 1 && j == s[i - 1]) || (i >= 2 && j == s[i - 2])) continue;
                    // 找到了一个可行字符，修改 s[i]
                    s[i] = j;
                    return i + 1;
                }
            }
            // 改 s[0] 都不行，无解
            return -1;
        };
        int pos = gao();
        if (pos == -1) return "";
        // s[pos] 到 s[n - 1] 贪心填入与前两个字符不同的最小字符即可
        for (int i = pos; i < n; i++) {
            // 枚举字母表前 k 个字符
            for (int j = 'a'; j < k + 'a'; j++) {
                // 当前字符和前两个字符中的某一个相同，不行
                if ((i >= 1 && j == s[i - 1]) || (i >= 2 && j == s[i - 2])) continue;
                // 找到了一个可行字符，修改 s[i]，并继续修改下一个字符
                s[i] = j;
                break;
            }
        }
        return s;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/WvYA94/view/shXgau/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。