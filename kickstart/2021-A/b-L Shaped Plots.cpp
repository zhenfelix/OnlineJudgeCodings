#include <bits/stdc++.h>

using namespace std;

inline bool valid(int x, int len){
    return 0 <= x && x < len;
}

inline int calc(int a, int b){
    int cur = 0;
    if (a < 2 || b < 2)
        return 0;
    cur += min(a-1, (b-2)/2);
    cur += min((a-2)/2, b-1);
    return cur;
}

class Solution
{
public:
    int countShape(vector<vector<int>> &mat, int n, int m)
    {
        const vector<pair<int, int>> dxy = {{1, 1}, {1, -1}, {-1,-1}, {-1,1}};
        const vector<pair<int,int>> start_xy = {{0,0}, {0,m-1},{n-1,m-1},{n-1,0}};
        
        int cnt = 0;
        for (int idx = 0; idx < 4; idx++){
            vector<vector<int>> dp_a(n, vector<int>(m, 0)), dp_b(n, vector<int>(m, 0));
            auto [dx, dy] = dxy[idx];
            auto [start_x, start_y] = start_xy[idx];
            for (int x = start_x; valid(x, n); x += dx){
                for (int y = start_y; valid(y, m); y += dy){
                    if (mat[x][y] == 0)
                        continue;
                    // cout << x << " " << y << endl;
                    dp_a[x][y] = dp_b[x][y] = mat[x][y];
                    if (valid(x-dx, n))
                        dp_a[x][y] += dp_a[x-dx][y];
                    if (valid(y-dy, m))
                        dp_b[x][y] += dp_b[x][y-dy];
                    cnt += calc(dp_a[x][y], dp_b[x][y]);
                }
            }
        }
        return cnt;
    }
};



int main()
{
    // freopen("input", "r", stdin);
    Solution sol;
    int T, R, C, idx = 1;
    cin >> T;
    while (T--)
    {
        cin >> R >> C;
        vector<vector<int>> mat(R, vector<int>(C));
        for (int i = 0; i < R; i++){
            for (int j = 0; j < C; j++)
                cin >> mat[i][j];
        }
        cout << "Case #" << idx++ << ": " << sol.countShape(mat, R, C) << endl;
    }
}