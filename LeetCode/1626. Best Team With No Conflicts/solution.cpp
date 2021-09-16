// class Solution {
// public:
//     int bestTeamScore(vector<int>& scores, vector<int>& ages) {
//         int n = scores.size();
//         vector<int> dp(n);
//         vector<pair<int,int>> sa;
//         for (int i = 0; i < n; i++){
//             sa.push_back({ages[i],scores[i]});
//         }
//         sort(sa.begin(), sa.end());
//         for (int i = 0; i < n; i++){
//             auto [a,s] = sa[i];
//             dp[i] = s;
//             for (int j = 0; j < i; j++){
//                 if (sa[j].second <= sa[i].second)
//                     dp[i] = max(dp[i], dp[j]+s);
//             }
//         }
//         return *max_element(dp.begin(), dp.end());
//     }
// };




// class Solution {
// public:
//     int bestTeamScore(vector<int>& scores, vector<int>& ages) {
//         int n = scores.size();
//         vector<int> dp(n);
//         vector<pair<int,int>> sa;
//         for (int i = 0; i < n; i++){
//             sa.push_back({scores[i],ages[i]});
//         }
//         sort(sa.begin(), sa.end());
//         for (int i = 0; i < n; i++){
//             auto [s,a] = sa[i];
//             dp[i] = s;
//             for (int j = 0; j < i; j++){
//                 if (sa[j].second <= sa[i].second)
//                     dp[i] = max(dp[i], dp[j]+s);
//             }
//         }
//         return *max_element(dp.begin(), dp.end());
//     }
// };

const int maxn = 1005;
int dp[maxn];


class Solution {
public:
    int query(int x){
        int q = 0;
        while (x){
            q = max(dp[x], q);
            x -= (x&(-x));
        }
        return q;
    }
    void update(int x, int v){
        while (x <= maxn){
            dp[x] = max(dp[x], v);
            x += (x&(-x));
        }
    }
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        int n = scores.size();
        memset(dp, 0, maxn*sizeof(int));
        vector<pair<int,int>> sa;
        for (int i = 0; i < n; i++){
            sa.push_back({scores[i],ages[i]});
        }
        sort(sa.begin(), sa.end());
        int res = 0;
        for (int i = 0; i < n; i++){
            auto [s,a] = sa[i];
            s = query(a)+s;
            // cout << s << endl;
            res = max(res,s);
            update(a, s);
        }
        return res;
    }
};