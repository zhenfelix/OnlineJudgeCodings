
# 腾讯实习-2023.03.26-第四题-子数组异或和
# 题目内容

# 给出一个正整数数组 AA，牛牛想知道其中有多少子数组满足: 里面所有数字的乘积等于里面所有数字的异或。

# 一个数组的子数组指数组中非空的一段连续数字
# 输入描述

# 第一行一个正整数 nn，代表给出数组长度

# 第二行 nn 个空格分隔的正整数 AA;

# 1⩽n⩽1051⩽n⩽105

# 1⩽Ai⩽1091⩽Ai​⩽109
# 输出描述

# 输出一个正整数代表答案
# 样例

# 输入

# 3
# 1 2 1

# 输出

# 4

# 样例解释

# 数组 [1],[2],[1],[1,2,1][1],[2],[1],[1,2,1] 都是满足条件的。


#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <queue>
using namespace std;
using ll = long long;

int solve(int n, vector<int> &arr)
{
    vector<int> st(n+1);
    st[0] = -1;
    int l = 1, r = 1;
    ll s = 1;
    int INT_MAX = pow(2, 32) - 1;
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > 1)
            st[r++] = i;
        s *= arr[i];
        while (s > INT_MAX)
        {
            s /= arr[st[l]];
            l++;
        }
        int mul = 1, xor_val = 0;
        if (arr[i] == 1)
        {
            xor_val = (i - st[r-1]) & 1;
            ans += (i - st[r-1] + 1) / 2;
        }
        for (int j = r-1; j >= l; j--)
        {
            mul *= arr[st[j]];
            xor_val ^= arr[st[j]];
            int ones = st[j] - st[j - 1] - 1;
            if (mul == xor_val)
            {
                ans += ones / 2 + 1;
            }
            if (mul == (xor_val ^ 1))
            {
                ans += (ones + 1) / 2;
            }
        }
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // freopen("contests/input", "r", stdin);
    // string s;
    // int case;
    for (int i = 0; i < 1; i++)
    {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int j = 0; j < n; j++)
        {
            cin >> arr[j];
        }
        cout << solve(n, arr) << "\n";
    }
    return 0;
}
