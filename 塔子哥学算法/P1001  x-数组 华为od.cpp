
// x-数组
// 题目内容

// 塔子哥最近喜欢研究数组中子段是否存在一些特殊的关系，比如 x−子段x−子段 ,现在有人来找塔子哥帮忙寻找数组中子段的 x−子段x−子段,但是塔子哥现在很忙，你能帮他解决这个问题吗？

// 如果一个数组中出现次数最多的元素出现大于等于 xx 次， 被称为 x−子段x−子段。

// 现在给定一个数组 aa 和 xx ,试问 aa 有多少子段是 x−子段x−子段 。

//     子段是数组中一个或多个连续元素组成的数组。

// 输入描述

// 第一行输入两个整数 n≤10000n≤10000 和 x≤nx≤n 。 1≤ai≤n1≤ai​≤n

// 第二行输入 nn 个整数。
// 输出描述

// 输出给定的数组中有多少子数组是 x−子段x−子段
// 样例

// 输入

// 7 3
// 2 1 3 2 1 3 2

// 输出

// 1


#include<bits/stdc++.h>

using namespace std;
using ll = long long;

using pii = pair<int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    
    int n, x;
    const int inf = 0x3f3f3f3f;
    cin >> n >> x;
    vector<int> arr(n,0), cnt(n+1,0);
    int l = 0, r = 0;
    ll ans = 0;
    for (;r < n; r++){
        cin >> arr[r];
        cnt[arr[r]]++;
        while (l <= r && cnt[arr[r]] >= x) {
            cnt[arr[l++]]--;
        }
        ans += l;
    }
    cout << ans << endl;
    return 0;
}