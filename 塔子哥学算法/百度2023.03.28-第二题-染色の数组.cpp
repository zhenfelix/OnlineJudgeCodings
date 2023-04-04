
// 2023.03.28-第二题-染色の数组
// 题目内容

// 塔子哥有一个神奇的序列，其中一些数字被染成白色，另外一些数字被染成黑色。塔子哥准备在其中选出两个数，这两个数恰好是一白一黑，选出的两个数的乘积为选择的方案权值。塔子哥想知道，所有合法的选数方案的权值之和是多少?答案可能过大，请对109+7109+7取模。
// 输入描述

// 第一行输入一个正整数nn，代表数组的大小。

// 第二行输入nn个正整数aiai​，代表塔子哥拿到的数组。

// 第三行输入一个仅由R和B组成的长度为nn的字符串，第ii个字符是R代表第ii个元素被染成白色，B代表染成黑色

// 1⩽n⩽1051⩽n⩽105

// 1⩽ai⩽1091⩽ai​⩽109
// 输出描述

// 最终的权值之和对109+7109+7取模的值。
// 样例

// 输入

// 4
// 1 2 1 2
// RRBB

// 输出

// 9


#include<bits/stdc++.h>

using namespace std;
using ll = long long;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input","r",stdin);
    const int MOD = 1e9+7;
    int n;
    ll r = 0, b = 0;
    cin >> n;
    vector<int> arr(n);
    string s;
    for (int i= 0; i < n; i++) cin >> arr[i];
    cin >> s;
    for (int i = 0; i < n; i++){
        if (s[i] == 'R') r += arr[i];
        else b += arr[i];
    }
    cout << ((r%MOD)*(b%MOD))%MOD << endl;
    return 0;
}