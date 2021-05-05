#include <bits/stdc++.h>

using namespace std;
const int inf = 0x3f3f3f3f;

class Solution
{
public:
    int minOps(string &s, int n, int k)
    {
        int i = 0, j = n - 1;
        while (i <= j)
        {
            if (s[i] != s[j])
                k--;
            i++;
            j--;
        }
        return abs(k);
    }
};

int main()
{
    // freopen("input", "r", stdin);
    Solution sol;
    int T, N, K, idx = 1;
    string s;
    cin >> T;
    while (T--)
    {
        cin >> N >> K;
        cin >> s;
        cout << "Case #" << idx++ << ": " << sol.minOps(s, N, K) << endl;
    }
}