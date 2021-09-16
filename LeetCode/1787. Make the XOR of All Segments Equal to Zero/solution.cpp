const int inf = 0x3f3f3f3f;
const int maxn = 1<<10;

class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> tot(k), dp(maxn,inf), ndp(maxn,inf);
        vector<unordered_map<int,int>> cnt(k);
        dp[0] = 0;
        for (int i = 0; i < n; i++){
            tot[i%k]++;
            cnt[i%k][nums[i]]++;
        }
        for (int i = 0; i < k; i++){
            int min_dp = *min_element(dp.begin(), dp.end()) + tot[i];
            for (int s = 0; s < maxn; s++){
                ndp[s] = min_dp;
                for (auto [k,v] : cnt[i]){
                    ndp[s] = min(ndp[s], dp[s^k]+tot[i]-v);
                }
            }
            swap(dp, ndp);
        }
        return dp[0];
    }
};




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



class Solution {
public:
    static constexpr int maxn = (1<<10)+5;
    static constexpr int inf = 0x3f3f3f3f;
    int dp[maxn], ndp[maxn];
    int minChanges(vector<int>& nums, int k) {
        int n = nums.size();
        memset(dp, inf, sizeof(int)*maxn);
        dp[0] = 0;
        for (int i = 0; i < k; i++){
            unordered_map<int,int> cnt;
            int total = 0;
            for (int j = i; j < n; j += k){
                if (cnt.find(nums[j]) == cnt.end())
                    cnt[nums[j]] = 0;
                cnt[nums[j]] += 1;
                total++;
            }
            int mi = *min_element(dp, dp+maxn);
            memset(ndp, inf, sizeof(int)*maxn);
            for (int x = 0; x < (1<<10); x++){
                ndp[x] = mi + total;
                for (const auto& [k, v] : cnt){
                    ndp[x] = min(ndp[x], dp[x^k]+total-v);
                }
            }
            swap(dp, ndp);

        }
        return dp[0];
        
    }
};