class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        auto gao = [&]() {
            int n = landStartTime.size(), m = waterStartTime.size();

            // 水上项目按开始时间排序
            typedef pair<int, int> pii;
            vector<pii> vec;
            for (int i = 0; i < m; i++) vec.push_back({waterStartTime[i], waterDuration[i]});
            sort(vec.begin(), vec.end());

            // 预处理后缀的最小结束时间
            int f[m];
            f[m - 1] = vec[m - 1].first + vec[m - 1].second;
            for (int i = m - 2; i >= 0; i--) f[i] = min(f[i + 1], vec[i].first + vec[i].second);

            // 陆上项目按结束时间排序
            vector<int> fin;
            for (int i = 0; i < n; i++) fin.push_back(landStartTime[i] + landDuration[i]);
            sort(fin.begin(), fin.end());

            // 双指针
            // i：当前枚举的陆上项目
            // j：开始时间不早于陆上项目结束时间的第一个水上项目
            // mn：前面的水上项目的最短持续时间
            int ans = 1e9, mn = 1e9;
            for (int i = 0, j = 0; i < n; i++) {
                while (j < m && vec[j].first < fin[i]) {
                    mn = min(mn, vec[j].second);
                    j++;
                }
                ans = min(ans, fin[i] + mn);
                if (j < m) ans = min(ans, f[j]);
            }
            return ans;
        };

        // 陆上项目先，水上项目后的情况
        int ans1 = gao();
        // 两种项目互换，求水上项目先，陆上项目后的情况
        swap(landStartTime, waterStartTime);
        swap(landDuration, waterDuration);
        int ans2 = gao();
        return min(ans1, ans2);
    }
};