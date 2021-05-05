#include <bits/stdc++.h>

using namespace std;

const int inf = 0x3f3f3f3f;

class Solution
{
public:
    bool reverseSort(vector<int> &arr, int cost)
    {
        int n = arr.size();
        for (int i = n-2; i >= 0; i--){
            if (cost <= i)
                return false;
            int right = min(n-1, i+cost-i-1);
            int left = i;
            cost -= (right-left+1);
            while (left < right)
                std::swap(arr[left++], arr[right--]);
        }
        return cost == 0;
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
    int T, N, C, idx = 1;
    cin >> T;
    while (T--)
    {
        cin >> N >> C;
        vector<int> arr;
        for (int i = 1; i <= N; i++)
            arr.push_back(i);
        if (sol.reverseSort(arr, C)){
            cout << "Case #" << idx++ << ":";
            for (auto x : arr){
                cout << " " << x;
            }
            cout << "\n";
        }
        else{
            cout << "Case #" << idx++ << ": " << "IMPOSSIBLE" << "\n";
        }
        
    }
}