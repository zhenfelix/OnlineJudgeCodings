#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int n = 100;
const int m = 10000;

class Solution
{
public:
    double maxPick(vector<int> &arr, int k)
    {
        vector<int> candidates;
        int res = 0, pre = 0, n = arr.size();
        sort(arr.begin(), arr.end());
        for (int i = 1; i < n; i++){
            int delta = arr[i]-arr[i-1]-1;
            if (delta > 0){
                res = max(res, delta);
                candidates.push_back((delta+1)/2);
            }
        }
        candidates.push_back(arr[0]-1);
        candidates.push_back(k-arr[n-1]);
        sort(candidates.begin(), candidates.end(), greater<int>());
        flog << "res before: " << res << endl;
        res = max(res, candidates[0]+candidates[1]);
        flog << "candidates : ";
        for (auto x : candidates)
            flog << x << " ";
        flog << "\n res : " << res << endl;
        return (double) res/k;
    }
};

const char *input = "/home/zhen/work/OnlineJudgeCodings/codejam/2021-qualification/test_data_e/test_set_2/ts2_input.txt";
const char *output = "/home/zhen/work/OnlineJudgeCodings/codejam/2021-qualification/test_data_e/test_set_2/ts2_output_.txt";

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);

    
    Solution sol;
    int T, N, K, idx = 1;

    cin >> T;
    while (T--)
    {
        cin >> N >> K;
        vector<int> vec(N);
        string line;
        for (int i = 0; i < N; i++)
        {
            cin >> vec[i];
        }
        cout << "Case #" << idx++ << ": " << sol.maxPick(vec, K) << endl;
    }
}