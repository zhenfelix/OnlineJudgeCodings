#include <bits/stdc++.h>


using namespace std;

const vector<pair<int, int>> dirs = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

class Solution
{
public:
    long long minBox(vector<vector<int>> &mat, int n, int m)
    {
        long long cnt = 0;
        priority_queue<tuple<int,int,int>> pq;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++)
                pq.push({mat[i][j],i,j});
        }
        while (!pq.empty()){
            auto [h, i, j] = pq.top(); pq.pop();
            if (h < mat[i][j])
                continue;
            for (auto [dx, dy] : dirs){
                dx += i; dy += j;
                if (dx < 0 || dx >= n || dy < 0 || dy >= m)
                    continue;
                if (mat[dx][dy] < h-1){
                    cnt += h-1-mat[dx][dy];
                    mat[dx][dy] = h-1;
                    pq.push({h-1,dx,dy});
                }
            }
        }
        return cnt;
    }
};

const char *input = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_c/test_set_1/ts1_input.txt";
const char *output = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_c/test_set_1/ts1_output_.txt";

int main()
{
    ios::sync_with_stdio(false);
    freopen(input, "r", stdin);
    freopen(output, "w", stdout);
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
        cout << "Case #" << idx++ << ": " << sol.minBox(mat, R, C) << "\n";
    }
}















#include <bits/stdc++.h>


using namespace std;

const vector<pair<int, int>> dirs = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

class Solution
{
public:
    long long minBox(vector<vector<int>> &mat, int n, int m)
    {
        long long cnt = 0;
        int mx = 0, total = n*m;
        unordered_map<int,vector<pair<int,int>>> mp;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                mx = max(mx, mat[i][j]);
                mp[mat[i][j]].push_back({i,j});
            }
                
        }
        
        for (int h = mx; h > mx-total; h--){
            for (auto [i,j] : mp[h]){
                if (h < mat[i][j])
                    continue;
                for (auto [dx, dy] : dirs){
                dx += i; dy += j;
                if (dx < 0 || dx >= n || dy < 0 || dy >= m)
                    continue;
                if (mat[dx][dy] < h-1){
                    cnt += h - 1 - mat[dx][dy];
                    mat[dx][dy] = h - 1;
                    mp[h - 1].push_back({dx, dy});
                }
            }
            }
        }
        return cnt;
    }
};

const char *input = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_c/test_set_2/ts2_input.txt";
const char *output = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_c/test_set_2/ts2_output_.txt";

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
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
        cout << "Case #" << idx++ << ": " << sol.minBox(mat, R, C) << "\n";
    }
}