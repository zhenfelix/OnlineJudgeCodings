
class Solution {
public:
    int minDistance(vector<int>& houses, int K) {
     int n = houses.size();
     sort(houses.begin(), houses.end());
     vector<int> presums = {0};
     for (int i = 0; i < n; i++)
         presums.push_back(presums.back()+houses[i]);
     auto calc = [&](int left, int right){
         int mid = (left+right)/2;
         int lc = mid-left+1, rc = right-mid;
         return houses[mid]*lc-(presums[mid+1]-presums[left])+presums[right+1]-presums[mid+1]-houses[mid]*rc;
     };

     vector<vector<int>> dp(K+1,vector<int>(n,0));
     for (int i = 1; i < n; i++)
         dp[1][i] = calc(0,i);
     for (int k = 2; k <= K; k++){
         for (int i = k; i < n; i++){
             dp[k][i] = INT_MAX;
             for (int j = i-1; j >= k-2; j--){
                    int cost = calc(j+1,i);
                    if (cost >= dp[k][i])
                        break;
                    dp[k][i] = min(dp[k][i], dp[k-1][j]+cost);
                }
             // for (int j = k-2; j < i; j++)
             //     dp[k][i] = min(dp[k][i], dp[k-1][j]+calc(j+1,i));
         }
     }
     return dp[K][n-1];
    }
};


int pre[105][105], dp[105][105];
class Solution {
public:
    int minDistance(vector<int>& houses, int k) {
        memset(dp, 0x3f, sizeof dp);
        memset(pre, 0, sizeof pre);

        int n = houses.size();
        sort(houses.begin(), houses.end());
        for(int i = n - 2; ~i; i -= 1)
            for(int j = i + 1; j < n; j += 1) 
                pre[i][j] = pre[i + 1][j - 1] + houses[j] - houses[i];
        for(int i = 0; i < n; i += 1) {
            dp[i][1] = pre[0][i];
            for(int j = 2; j <= k && j <= i + 1; j += 1) 
                for(int i0 = 0; i0 < i; i0 += 1) 
                    dp[i][j] = min(dp[i][j], dp[i0][j - 1] + pre[i0 + 1][i]);        
        }
        return dp[n - 1][k];
    }
};



DP的决策单调性优化总结 https://www.luogu.com.cn/blog/command-block/dp-di-jue-ce-dan-diao-xing-you-hua-zong-jie


constexpr int maxn = 100;
constexpr int inf = 10000000;
int h[maxn + 1], s[maxn + 1];
int dp[maxn + 1];
int ndp[maxn + 1];
int f(int l, int r){
    int res = s[r] + s[l - 1] - s[(l + r) / 2] * 2;
    if((r - l) % 2 == 0) res += h[(l + r) / 2];
    return res;
}

void DC(int L, int R, int l, int r){
    int M = (L + R) >> 1, p = l;
    for(int i = l + 1; i <= r and i < M; i += 1) if(dp[i] + f(i + 1, M) < dp[p] + f(p + 1, M)) p = i;
    ndp[M] = dp[p] + f(p + 1, M);
    if(L < M) DC(L, M - 1, l, p);
    if(M < R) DC(M + 1, R, p, r);
}
class Solution {
public:
    int minDistance(vector<int>& houses, int k) {
        int n = houses.size();
        sort(houses.begin(), houses.end());
        for(int i = 1; i <= n; i += 1) s[i] = s[i - 1] + (h[i] = houses[i - 1]);
        for(int j = 0; j <= n; j += 1) dp[j] = inf;
        dp[0] = 0;

        for(int i = 1; i <= k; i += 1){
            DC(1, n, 0, n - 1);
            for(int i = 1; i <= n; i += 1) dp[i] = ndp[i];
        }
        return dp[n];
    }
};


// 作者：Heltion
// 链接：https://leetcode-cn.com/problems/allocate-mailboxes/solution/dong-tai-gui-hua-shi-jian-fu-za-du-oknlognkong-jia/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。