
# 腾讯实习-2023.03.26-第五题-牛妹的生日
# 题目内容

# 牛妹在生日这一天收到了一个长度为 nn 的序列 a1,a2,...,ana1​,a2​,...,an​。牛妹希望从这个序列中删除一些数,使得剩下的元素的最大公约数恰好等于 kk。

# 牛妹想知道有多少种删除的方宰。由于答室可能过大，请对 109+7109+7 取模

# 最大公约数:指两个或多个整数公有约数中最大的一个
# 输入描述

# 第一行输入两个正整数 n,kn,k

# 第二行输入 nn 个正整数代表 a1,a2,...,ana1​,a2​,...,an​

# 1⩽n,ai⩽1051⩽n,ai​⩽105
# 输出描述

# 输出一行整数，代表删除的方案数在109+7109+7 意义下的取值。
# 样例

# 输入

# 3 3
# 3 3 3

# 输出

# 7


#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <queue>

using namespace std;

const int MOD = 1e9 + 7;

int solve(int n, int k, vector<int> &arr)
{
    int mx = *max_element(arr.begin(), arr.end());
    vector<int> cc(mx + 1, 0);
    for (int a : arr)
        cc[a]++;
    vector<int> fs(n + 1, 1);
    for (int i = 1; i <= n; i++)
    {
        fs[i] = (2 * fs[i - 1]) % MOD;
    }
    for (int i = k; i <= mx; i++)
    {
        for (int j = i * 2; j <= mx; j += i)
        {
            cc[i] += cc[j];
        }
    }
    vector<int> dp(mx + 1, 0);
    int ans = 0;
    for (int i = mx; i >= k; i--)
    {
        dp[i] = fs[cc[i]] - 1;
        for (int j = i * 2; j <= mx; j += i)
        {
            dp[i] = (dp[i] - dp[j] + MOD) % MOD;
        }
        
    }
    return dp[k];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    // freopen("contests/input", "r", stdin);
    int t = 1;
    // cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> arr(n);
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        cout << solve(n, k, arr) << '\n';
    }
    return 0;
}
