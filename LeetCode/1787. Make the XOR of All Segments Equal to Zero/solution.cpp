const int INF = 0x3f3f3f3f;

class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        int n = nums.size();
        vector<unordered_map<int, int>> groups(k);
        vector<int> size(k);
        for (int i = 0; i < k; ++i) {
            for (int j = i; j < n; j += k) {
                groups[i][nums[j]]++;
                size[i]++;
            }
        }
        
        vector<int> dp(1 << 10, INF);
        dp[0] = 0;
        for (int i = 0; i < k; ++i) {
            int lo = *min_element(dp.begin(), dp.end());
            vector<int> ndp(1 << 10, lo + size[i]);
            for (int j = 0; j < (1 << 10); ++j) {
                // if (dp[j] == INF)
                //     continue;
                for (auto [p, freq] : groups[i]) {
                    int pre = p ^ j;
                    ndp[j] = min(ndp[j], dp[pre] + size[i] - freq);
                }
            }
            dp = move(ndp);
        }
        
        return dp[0];
    }
};

