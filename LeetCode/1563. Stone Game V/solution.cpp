// WA solution, greedy approach is wrong!
// class Solution {
// public:
//     int stoneGameV(vector<int>& stoneValue) {
//         int n = stoneValue.size();
//         vector<vector<int>> dp(n,vector<int>(n,0));
//         vector<int> presums = {0};
//         for (auto v : stoneValue)
//             presums.push_back(presums.back()+v);
//         for (int i = n-1; i >= 0; i--){
//             int k = i-1, left = 0, right = stoneValue[i];
//             for (int j = i+1; j < n; j++){
//                 right += stoneValue[j];
//                 while (k+1 < j && left+stoneValue[k+1] <= right-stoneValue[k+1]){
//                     k++;
//                     left += stoneValue[k];
//                     right -= stoneValue[k];
//                 }
//                 if (left == right){
//                     dp[i][j] = max(dp[i][k],dp[k+1][j])+left;
//                 }
//                 else{
//                     if (k >= i)
//                         dp[i][j] = max(dp[i][j], dp[i][k]+left);
//                     if (k+2 <= j)
//                         dp[i][j] = max(dp[i][j], dp[k+2][j]+right-stoneValue[k+1]);
//                 }
//             }
//         }
//         return dp[0][n-1];
//     }
// };





class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<vector<int>> dp(n,vector<int>(n,0)), mxl(n,vector<int>(n,0)), mxr(n,vector<int>(n,0));
        vector<int> presums = {0};
        for (auto v : stoneValue)
            presums.push_back(presums.back()+v);
        auto sum = [&](int i, int j){
            return presums[j+1]-presums[i];
        };

        for (int i = n-1; i >= 0; i--){
            int k = i-1, left = 0, right = stoneValue[i];
            mxl[i][i] = mxr[i][i] = stoneValue[i]; 
            for (int j = i+1; j < n; j++){
                right += stoneValue[j];
                while (k+1 < j && left+stoneValue[k+1] <= right-stoneValue[k+1]){
                    k++;
                    left += stoneValue[k];
                    right -= stoneValue[k];
                }
                if (left == right){
                    dp[i][j] = max(mxl[i][k],mxr[k+1][j]);
                }
                else{
                    if (k >= i)
                        dp[i][j] = max(dp[i][j], mxl[i][k]);
                    if (k+2 <= j)
                        dp[i][j] = max(dp[i][j], mxr[k+2][j]);
                }
                mxl[i][j] = max(mxl[i][j-1], dp[i][j]+sum(i,j));
                mxr[i][j] = max(mxr[i+1][j], dp[i][j]+sum(i,j));
            }
        }
        return dp[0][n-1];
    }
};

// const int N = 505;
// int s[N][N], g[N][N], f[N][N], mxl[N][N], mxr[N][N];
// class Solution {
// public:
// 	int stoneGameV(vector<int>& a) {
// 		int n = a.size();
// 		for (int i = 0; i < n; i++) {
// 			for (int j = 0; j < n; j++) {
// 				f[i][j] = g[i][j] = s[i][j] = 0;
// 				mxl[i][j] = mxr[i][j] = 0;
// 			}
// 		}
// 		for (int i = 0; i < n; i++) {
// 			s[i][i] = a[i];
//             g[i][i] = i;
//             for (int j = i + 1; j < n; j++) {
//                 s[i][j] = s[i][j - 1] + a[j];
//                 int now = g[i][j - 1];
//                 while (s[i][j] - s[i][now] > s[i][now]) {
//                     now++;
//                 }
//                 g[i][j] = now;
//             }
// 		}
        
// 		for (int len = 1; len <= n; len++) {
// 			for (int l = 0; l + len - 1 < n; l++) {
// 				int r = l + len - 1;
// 				int mid = g[l][r];
// 				int ls = s[l][mid];
// 				int rs = s[mid + 1][r];
// 				if (ls == rs) {
// 					f[l][r] = max(f[l][r], mxl[l][mid]);
// 					f[l][r] = max(f[l][r], mxr[mid + 1][r]);
// 				} else {
// 					if (mid > l) {
// 						int ls = s[l][mid - 1];
// 						f[l][r] = max(f[l][r], mxl[l][mid - 1]);
// 					}
// 					if (mid < r) {
// 						int rs = s[mid + 1][r];
// 						f[l][r] = max(f[l][r], mxr[mid + 1][r]);
// 					}
// 				}
// 				int v = f[l][r] + s[l][r];
// 				if (l == r) {
// 					mxl[l][r] = mxr[l][r] = v;
// 				} else {
// 					mxl[l][r] = max(v, mxl[l][r - 1]);
// 					mxr[l][r] = max(v, mxr[l + 1][r]);
// 				}
// 			}
// 		}
// 		return f[0][n - 1];
// 	}
// };


