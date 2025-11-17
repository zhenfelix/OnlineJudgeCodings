class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size(), ans = 0;

        // 子串只包含一个字母的情况
        auto calc1 = [&]() {
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (i == 0 || s[i] == s[i - 1]) cnt++;
                else cnt = 1;
                ans = max(ans, cnt);
            }
        };

        // 子串只包含两个字母的情况
        auto calc2 = [&](char a, char b) {
            unordered_map<int, int> mp;
            mp[0] = -1;

            // x 表示 a_i - b_i 的值
            int x = 0;
            for(int i = 0; i < n; i++) {
                if (s[i] == a) x++;
                else if (s[i] == b) x--;
                else {
                    // 遇到不在子串里的字符，截断
                    mp.clear();
                    x = 0;
                }
                if (mp.count(x)) ans = max(ans, i - mp[x]);
                else mp[x] = i;
            }
        };

        // 子串包含三个字母的情况
        auto calc3 = [&]() {
            unordered_map<long long, int> mp;
            mp[0] = -1;

            // x 表示 a_i - b_i 的值
            // y 表示 b_i - c_i 的值
            int x = 0, y = 0;
            for (int i = 0; i < n; i++) {
                if (s[i] == 'a') x++;
                else if (s[i] == 'b') x--, y++;
                else y--;
                // c++ 的 unordered_map 不支持用 pair 作为 key
                // 所以只能把数对映射成一个整数
                // 当然也可以直接用 map，用 pair 作为 key
                // 只是复杂度会乘上一个 log
                long long key = 10LL * x * n + y;
                if (mp.count(key)) ans = max(ans, i - mp[key]);
                else mp[key] = i;
            }
        };

        calc1();
        calc2('a', 'b');
        calc2('a', 'c');
        calc2('b', 'c');
        calc3();
        return ans;
    }
};