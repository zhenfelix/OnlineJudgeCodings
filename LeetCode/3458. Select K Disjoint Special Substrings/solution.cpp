class Solution {
public:
    bool maxSubstringLength(string s, int K) {
        int n = s.size();

        vector<int> pos[26];
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            pos[c].push_back(i);
        }

        typedef pair<int, int> pii;
        vector<pii> vec;
        // 枚举每一种子串
        for (int i = 0; i < 26; i++) if (!pos[i].empty()) {
            // 一开始先用这种字母的范围作为子串的范围
            int l = pos[i][0], r = pos[i].back();
            bool flag = true;
            while (flag) {
                flag = false;
                // 检查子串里是否出现了其它字母
                for (int j = 0; j < 26; j++) {
                    int cnt = upper_bound(pos[j].begin(), pos[j].end(), r) - lower_bound(pos[j].begin(), pos[j].end(), l);
                    if (cnt > 0 && cnt < pos[j].size()) {
                        // 有一种字母没有被完全包含，用它的范围更新子串的范围
                        l = min(l, pos[j][0]);
                        r = max(r, pos[j].back());
                        flag = true;
                    }
                }
            }
            // 得到了这种子串里的最短子串
            if (l > 0 || r < n - 1) vec.push_back({r, l});
        }

        // leetcode 435. 无重叠区间
        sort(vec.begin(), vec.end());
        int R = -1, cnt = 0;
        for (pii p : vec) if (p.second > R) {
            R = p.first;
            cnt++;
        }
        return cnt >= K;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/SoR3j0/view/pgyMOB/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。