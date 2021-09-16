const int maxn = 31;
vector<vector<int>> dp(maxn,vector<int>(maxn,1));
bool initialized = false;

class Solution {
public:
    void init(){
        for (int i = 0; i < maxn; i++){
            for (int j = 1; j < i; j++)
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
        }
        initialized = true;
    }
    string kthSmallestPath(vector<int>& destination, int k) {
        if (!initialized)
            init();
        int row = destination[0], col = destination[1];
        int len = row+col;
        string res(len,'H');
        for (int i = 0; i < len; i++){
            if (col == 0 || k > dp[row+col-1][col-1]){
                if (col > 0)
                    k -= dp[row+col-1][col-1];
                res[i] = 'V';
                row--;
            }
            else
                col--;
            // cout << i << ' ' << res << endl;
        }
        return res;
    }
};