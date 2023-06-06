// 题目内容

// 设 AA 和 BB 的二进制表示为 an,an−1,⋯,a1an​,an−1​,⋯,a1​ 和 bn,bn−1,⋯,b1bn​,bn−1​,⋯,b1​ ，其中 ai,bi∈{0,1}ai​,bi​∈{0,1} ，

// 则它们的差异值为 ∑i=1n(ai∧bi)2i−1∑i=1n​(ai​∧bi​)2i−1 ，

// 相似值为 ∑i=1n(ai & bi)2i−1∑i=1n​(ai​ & bi​)2i−1 , 其中 ∧ 表示异或运算， & 表示与运算。

// 给定 nn 个正整数 A1,A2,⋯,AnA1​,A2​,⋯,An​ ，求满足 AiAi​ 和 AjAj​ 的差异值大于相似值的 (i,j)(i,j) 对数，其中 0≤i<j<n0≤i<j<n 。
// 输入描述

// 输入第一行为一个整数 nn ，表示数组的大小。

// 输入第二行为 nn 个整数，第 ii 个元素为 AiAi​ 。

// 1≤n≤1051≤n≤105 ， 1≤Ai≤2301≤Ai​≤230
// 输出描述

// 输出为一个整数，表示满足差异值大于相似值的对数。
// 样例
// 样例一

// 输入

// 4
// 4 3 5 2

// 输出

// 4

// 样例解释

// 有如下4组数据符合条件: (1,2),(1,3),(2,4),(3,4).(1,2),(1,3),(2,4),(3,4).
// 样例二

// 输入

// 5
// 1 2 3 4 5

// 输出

// 8

// 样例解释

// 有如下8组数据符合条件: (1,2),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5).(1,2),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5).
// 样例三

// 输入

// 5
// 16 36 35 40 2

// 输出

// 7

// 样例解释

// 有如下7组数据符合条件: (1,2),(1,3),(1,4),(1,5),(2,5),(3,5),(4,5).(1,2),(1,3),(1,4),(1,5),(2,5),(3,5),(4,5).


// #include <bits/stdc++.h>
// using namespace std;
// using ll = long long;

// int main() {
//     int n;
//     cin >> n;
//     map<int,int> mp;
//     for (int i = 0; i < n; i++) {
//         int a;
//         cin >> a;
//         mp[a]++;
//     }
//     vector<int> cnt(32,0);
//     ll ans = 0;
//     for (auto it = mp.begin(); it != mp.end(); ++it) {
//         auto [k,v] = *it;
//         int x = k;
//         for (int i = 0;;i++) {
//             if (x == 1) {
//                 cnt[i]+=v;
//                 break;
//             }
//             ans += (ll)(v*cnt[i]);
//             x >>= 1;
//         }
//     }
//     cout << ans << endl;
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<int> cnt(32,0);
    ll ans = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        for (int i = 0;;i++) {
            if (x == 1) {
                cnt[i]+=1;
                break;
            }
            x >>= 1;
        }
    }
    
    for (int i = 0; i < 32; i++) {
        ans += (ll) (cnt[i]) * (n-cnt[i]);
    }
    cout << ans/2 << endl;
    return 0;
}