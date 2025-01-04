using ll = long long;

class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        int n = board.size(), m = board[0].size();
        vector<vector<int>> bottom(n, vector<int>(m));
        
        // Copy board to bottom
        for (int i = 0; i < n; i++) {
            bottom[i] = board[i];
        }
        
        // Fill the bottom array with maximums from bottom up
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < m; j++) {
                bottom[i][j] = max(bottom[i][j], bottom[i + 1][j]);
            }
        }
        
        ll ans = LLONG_MIN;
        vector<vector<int>> mx(m, vector<int>(m, INT_MIN));
        
        // Initialize top with the first row
        vector<int> top = board[0];
        
        // Iterate through rows from the second to the second-to-last
        for (int i = 1; i < n - 1; i++) {
            vector<int> tmp = bottom[i + 1];
            sort(tmp.begin(), tmp.end());
            
            for (int p = 0; p < m; p++) {
                for (int q = p + 1; q < m; q++) {
                    int a = min(bottom[i + 1][p], bottom[i + 1][q]);
                    int b = max(bottom[i + 1][p], bottom[i + 1][q]);
                    
                    if (b < tmp[m-2] || (b == tmp[m-2] && a <= tmp[m-3])) {
                        mx[p][q] = mx[q][p] = tmp[m-1];
                    } else if (b < tmp[m-1] || (b == tmp[m-1] && a <= tmp[m-3])) {
                        mx[p][q] = mx[q][p] = tmp[m-2];
                    } else {
                        mx[p][q] = mx[q][p] = tmp[m-3];
                    }
                }
            }
            
            // Calculate the maximum possible sum
            for (int p = 0; p < m; p++) {
                for (int q = 0; q < m; q++) {
                    if (p == q) continue;
                    ans = max(ans, (ll)mx[p][q] + (ll)board[i][p] + (ll)top[q]);
                }
            }
            
            // Update top array
            for (int q = 0; q < m; q++) {
                top[q] = max(top[q], board[i][q]);
            }
        }
        
        return ans;
    }
};