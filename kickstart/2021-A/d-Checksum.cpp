#include <bits/stdc++.h>


using namespace std;


class Solution
{
public:
    long long minCost(vector<vector<int>> &mat, vector<vector<int>> &costs, int n)
    {
        int total = 0;
        vector<vector<int>> edges(2*n, vector<int>(2*n, 0));
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (mat[i][j] == -1){
                    edges[n+j][i] = edges[i][n+j] = costs[i][j];
                    total += costs[i][j];
                }
            }
        }
        vector<int> candidates(2*n, 0);
        vector<bool> visited(2*n, false);
        
        for (int i = 0; i < 2*n; i++){
            int v = -1;
            for (int j = 0; j < 2*n; j++){
                if (!visited[j] && (v == -1 || candidates[j] > candidates[v])){
                    v = j;
                }
            }
            visited[v] = true;
            total -= candidates[v];
            for (int j = 0; j < 2*n; j++){
                if (!visited[j] && edges[v][j] > candidates[j]){
                    candidates[j] = edges[v][j];
                }
            }
        }
        return total;
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
    int T, N, idx = 1;
    cin >> T;
    while (T--){
        cin >> N;
        vector<vector<int>> mat(N, vector<int>(N)), costs(N, vector<int>(N));
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                cin >> mat[i][j];
            }
                
        }
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                cin >> costs[i][j];
            }
        }
        string tmp;
        getline(cin, tmp);
        getline(cin, tmp);
        getline(cin, tmp);
        cout << "Case #" << idx++ << ": " << sol.minCost(mat, costs, N) << "\n";
    }
}