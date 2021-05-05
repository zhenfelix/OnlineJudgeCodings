#include <bits/stdc++.h>


using namespace std;

const int inf = 0x3f3f3f3f;

class Solution
{
public:
    long long minCost(vector<int> &arr, int n)
    {
        int total = 0;
        for (int i = 0; i < n-1; i++){
            int mi = inf, idx = -1;
            for (int j = i; j < n; j++){
                if (arr[j] < mi){
                    mi = arr[j];
                    idx = j;
                }
            }
            total += idx-i+1;
            int left = i, right = idx;
            while (left < right){
                std::swap(arr[left++], arr[right--]);
            }
        }
        return total;
    }
};

const char *input = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_input.txt";
const char *output = "/home/zhen/work/OnlineJudgeCodings/kickstart/2021-A/test_data_d/test_set_3/ts3_output_.txt";

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
        vector<int> arr(N);
        for (int i = 0; i < N; i++){
            cin >> arr[i];
        }

        cout << "Case #" << idx++ << ": " << sol.minCost(arr, N) << "\n";
    }
}