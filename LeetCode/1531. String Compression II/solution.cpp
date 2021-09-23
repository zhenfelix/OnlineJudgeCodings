int dp[111][111];
class Solution {
public:
    int getLengthOfOptimalCompression(string s, int k) {
        int n = s.size();
        memset(dp, 0x3f, sizeof(dp));
        dp[0][0] = 0;
        for(int i = 1; i <= n; i++) {
            for(int j = 0; j <= k; j++) {
                dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j]);
                int cnt = 0, del = 0;
                for(int l = i; l <= n; l++) {
                    cnt += s[l - 1] == s[i - 1];
                    del += s[l - 1] != s[i - 1];
                    if(j + del <= k) dp[l][j + del] = min(dp[l][j + del], dp[i - 1][j] + 1 + (cnt >= 100 ? 3 : cnt >= 10 ? 2 : cnt >= 2 ? 1: 0));
                }
            }
        }
        return dp[n][k];
    }
};



const int inf = 0x3f3f3f3f;
const int maxn = 105;

int dp[maxn][maxn];

class Solution {
public:
    inline int calc(int x){
        return x <= 1 ? x : x <= 9 ? 2 : x <= 99 ? 3 : 4;
    }
    int getLengthOfOptimalCompression(string s, int K) {
        int n = s.length();
        memset(dp, 0x3f, maxn*maxn*sizeof(int));
        dp[0][0] = 0;
        for (int k = 0; k <= K; k++){
            for (int i = 1; i <= n; i++){
                if (k)
                    dp[k][i] = dp[k-1][i-1];
                int diff = 0, same = 0;
                for (int j = i; j >= 1 && k >= diff; j--){
                    same += (s[j-1] == s[i-1]);
                    diff += (s[j-1] != s[i-1]);
                    if (s[j-1] == s[i-1]){
                        dp[k][i] = min(dp[k][i], calc(same)+dp[k-diff][j-1]);
                    }
                }
            }
        }
        return dp[K][n];
    }
};