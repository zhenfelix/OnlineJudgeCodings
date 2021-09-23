const int maxnn = 50, maxn = 25, maxm = 8, maxk = 10;
int cb[maxnn][maxm];
bool initialized = false;
bool visited[maxk][maxn][maxk][maxn][maxk];
double dp[maxk][maxn][maxk][maxn][maxk];

class Solution {
    int n,k;
    vector<int> balls;
public:
    void init(){
        for (int i = 0; i < maxnn; i++){
            cb[i][0] = 1;
            if (i < maxm)
                cb[i][i] = 1;
        }
        for (int i = 1; i < maxnn; i++){
            for (int j = 1; j < min(i,maxm); j++)
                cb[i][j] = cb[i-1][j-1]+cb[i-1][j];
        }
        initialized = true;
    }
    double dfs(int i, int cl, int ul, int cr, int ur){
        if (cl > n || cr > n || ul > k-i+ur || ur > k-i+ul)
            return 0;
        if (i == k)
            return ul == ur ? 1 : 0;
        if (visited[i][cl][ul][cr][ur])
            return dp[i][cl][ul][cr][ur];
        dp[i][cl][ul][cr][ur] = 0;
        for (int j = 0; j <= balls[i]; j++){
            if (j > n-cl || balls[i]-j > n-cr)
                continue;
            dp[i][cl][ul][cr][ur] += (double)cb[n-cl][j]*cb[n-cr][balls[i]-j]*dfs(i+1,cl+j,ul+(j>0),cr+balls[i]-j,ur+(balls[i]-j>0))/cb[n*2-cl-cr][balls[i]];
        }
        visited[i][cl][ul][cr][ur] = 1;
        return dp[i][cl][ul][cr][ur];

    }
    double getProbability(vector<int>& balls) {
        init();
        memset(visited, 0, sizeof(bool)*maxk*maxk*maxk*maxn*maxn);
        k = balls.size();
        n = accumulate(balls.begin(), balls.end(), 0);
        n /= 2;
        this->balls = balls;
        return dfs(0,0,0,0,0);

    }
};