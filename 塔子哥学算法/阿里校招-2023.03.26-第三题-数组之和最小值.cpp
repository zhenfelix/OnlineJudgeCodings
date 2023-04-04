
# 阿里校招-2023.03.26-第三题-数组之和最小值
# 题目内容

# 给定一个数组，你可以进行最多k次以下操作：

# 选择一个大于1的元素 aiai​ ，使得 aiai​ 除以它的一个素因子pp。

# 试求操作结束后，数组的所有元素之和的最小值是多少？
# 输入描述

# 第一行输入两个正整数nn和kk，代表数组大小以及操作次数。

# 第二行输入nn个正整数aiai​，代表数组的元素。

# 1≤n,k≤2000001≤n,k≤200000

# 1≤ai≤1061≤ai​≤106
# 输出描述

# 一个整数，代表操作后的所有元素最小的和。
# 样例

# 输入

# 2 1
# 5 6

# 输出

# 7

# 样例解释

# 只能操作一次，选择一个元素，5／5＝1即可，数组变成[1,6]。


#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll solve(int n, int k, vector<int> &arr)
{
    int mx = *max_element(arr.begin(), arr.end());
    ll tot = accumulate(arr.begin(), arr.end(), 0ll);
    vector<int> f(mx + 1);
    for (int i = 2; i <= mx; ++i)
    {
        if (f[i] != 0)
            continue;
        f[i] = i;
        for (int j = i * 2; j <= mx; j += i)
        {
            f[j] = i;
        }
    }
    priority_queue<int, vector<int>, greater<>> hq;
    for (int a : arr)
    {
        while (a > 1)
        {
            hq.push(a / f[a] - a);
            a /= f[a];
        }
    }
    for (int i = 0; i < k; ++i)
    {
        if (hq.empty())
            break;
        tot += hq.top();
        hq.pop();
    }
    return tot;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    // freopen("contests/input", "r", stdin);
    // string s;
    // int case_;
    for (int i = 0; i < 1; ++i)
    {
        int n, k;
        cin >> n >> k;
        vector<int> arr(n);
        for (int j = 0; j < n; ++j)
        {
            cin >> arr[j];
        }
        // vector<int> brr(n);
        // for (int j = 0; j < n; ++j) {
        //     cin >> brr[j];
        // }
        // cin >> s;
        // vector<int> prizes(n);
        // for (int j = 0; j < n; ++j) {
        //     cin >> prizes[j];
        // }
        // vector<int> persons(n);
        // for (int j = 0; j < n; ++j) {
        //     cin >> persons[j];
        // }
        // n = rand() % 1000 + 1;
        cout << solve(n, k, arr) << '\n';
        // double ans = solve(s);
        // cout << fixed << setprecision(3) << ans << '\n';
        // cout << fixed << setprecision(3) << 0.0 << '\n';
        // int m = verify(s);
        // assert(m == n);
        // cout << n << ' ' << s << " ok\n";
        // cout << get_num_without_prize(persons, prizes) << '\n';
        // cout << solve(n, l, r) << '\n';
        // if (solve(n, l, r)) {
        //     cout << "Yes\n";
        // } else {
        //     cout << "No\n";
        // }
    }
    // int a, b;
    // for (int i = 0; i < 1000; ++i) {
    //     b = rand() % 10000000 + 1;
    //     a = rand() % b + 1;
    //     assert(solve(a, b) == solve_another(a, b));
    //     cout << i << ' ' << a << ' ' << b << " ok\n";
    // }
    return 0;
}