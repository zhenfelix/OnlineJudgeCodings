// class Solution {
// public:
//     vector<vector<unordered_map<int,int>>> memo;
//     int maxValue(vector<vector<int>>& events, int k) {
//         int n=events.size();
//         memo=vector<vector<unordered_map<int,int>>>(n,vector<unordered_map<int,int>>(k+1));
//         sort(events.begin(),events.end(),[](vector<int>& v1, vector<int>& v2){
//             return v1[0]<v2[0];
//         });
//         return dfs(0,events,k,0);
//     }
    
//     int dfs(int idx, vector<vector<int>>& events, int k, int end){
//         if(idx==events.size() || k==0) return 0;
        
//         if(memo[idx][k].find(end)!=memo[idx][k].end()) return memo[idx][k][end];
//         int res=dfs(idx+1,events,k,end);
        
//         if(events[idx][0]>end){
//             int candi=events[idx][2]+dfs(idx+1,events,k-1,events[idx][1]);
//             res=max(res,candi);
//         }
//         return memo[idx][k][end]= res;
//     }
// };


class Solution {
public:
    static bool cmp(const vector<int>& x, const vector<int>& y) {
        return x[1] < y[1];
    }
    int maxValue(vector<vector<int>>& events, int k) {
        int n = events.size();
        sort(events.begin(), events.end(), cmp);
        
        vector<vector<int>> dp(n, vector<int>(k + 1, INT_MIN));
        dp[0][0] = 0;
        dp[0][1] = events[0][2];
        
        for (int i = 1; i < n; i++) {
            // 参加会议 i，此时需要二分查找
            int l = 0, r = i;
            while (r - l > 1) {
                int mid = (l + r) / 2;
                if (events[mid][1] >= events[i][0]) {
                    r = mid;
                } else {
                    l = mid;
                }
            }
            if (events[l][1] < events[i][0]) {
                for (int j = 1; j <= k; j++) {
                    dp[i][j] = max(dp[i][j], dp[l][j-1] + events[i][2]);
                }
            } else {
                dp[i][1] = max(dp[i][1], events[i][2]);
            }
            
            // 不参加会议 i
            for (int j = 0; j <= k; j++) {
                dp[i][j] = max(dp[i][j], dp[i-1][j]);
            }
        }
        
        int ret = 0;
        for (int i = 0; i <= k; i++) {
            ret = max(ret, dp[n-1][i]);
        }
        return ret;
    }
};


// 作者：Arsenal-591
// 链接：https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended-ii/solution/dong-tai-gui-hua-er-fen-sou-suo-zui-duo-7c423/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。