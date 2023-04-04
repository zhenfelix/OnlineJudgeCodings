
// 2023.04.01-第三题-塔子哥的收藏夹
// 题目内容

// 塔子哥是一个热爱收藏的年轻人，他喜欢收集各种有趣的物品，例如邮票、硬币、瓶盖等等。他的收藏品越来越多，于是他决定为自己在收藏架上建了一排 nn 个收藏夹，分别编号为 1,2,3…n1,2,3…n。这样，他就可以更好地组织和展示自己的收藏品了。

// 塔子哥有些时候会突发奇想改变某一个收藏美里的内容，例如从中拿入、拿出一些藏品，这些的操作会改变塔子哥对这个收藏夹的欣赏程度，我们记编号为 ii 的收藏夹，塔子哥对其的欣赏程度为 aiai​ 。塔子哥在休息时间经常会欣赏连续编号的收藏夹，例如编号为 L,L+1,L+2,...,R−1,RL,L+1,L+2,...,R−1,R 的这些收藏夹，他能从中获得的满足感为这些收藏失的欣赏程度之和，即 ∑i=LRai∑i=LR​ai​ 。

// 塔子哥想在欣赏之前提前估算自己能得到的满足感，想知道如果他选择编号区间为 [L,R][L,R] 的收藏夹，能给他带来的满足感是多少。但是塔子哥不想自己计算，所以他想你帮他计算一下，然后告诉他。
// 输入描述

// 第一行两个整数 nn 和 mm ，表示塔子哥的收藏夹数量和塔子哥的操作数量。初始时刻收藏夹都是空的，也即 ai=0ai​=0 （ i∈[1,n]i∈[1,n] ）

// 第二行 mm 个整数 op1,op2,…,opmop1​,op2​,…,opm​ 。

// 第三行 mm 个整数 x1,x2,…,xmx1​,x2​,…,xm​ 。

// 第四行 mm 个整数 y1,y2,…,ymy1​,y2​,…,ym​ ，这些共同表示了 mm 次操作，对于第 ii 次操作， opi=0opi​=0 时表示为一次收藏夹更新操作，会将 xixi​ 位置的收藏夹欣赏程度更新为 yiyi​ ，即 axi=yiaxi​​=yi​ ； opi=1opi​=1 时表示为一次查询操作，表示如果塔子哥欣赏编号在区间 [xi,yi][xi​,yi​] 的收藏夹，能获得的满足感是多少，也即 ∑j=xiyiaj∑j=xi​yi​​aj​ 。

// 对于所有的数据， 1≤n,m≤50000,opi∈[0,1]1≤n,m≤50000,opi​∈[0,1] ，当 opi=0opi​=0 时， 1≤xi≤n,0≤yi≤100001≤xi​≤n,0≤yi​≤10000 ；当 opi=1opi​=1 时， 1≤xi≤yi≤n1≤xi​≤yi​≤n ，保证至少有一次 opi=1opi​=1 的操作。
// 输出描述

// 对每一个 opi=1opi​=1 的操作，输出一个数表示对应答案。空格隔开所有答案。
// 样例

// 输入

// 4 7
// 1 0 1 0 1 0 1
// 1 1 1 3 1 4 1
// 3 2 3 5 3 100 3

// 输出

// 0 2 7 7

// 样例解释 操作记录为

// 0 0 0 0(初始)

// 询问[1,3]结果为0+0+0>

// 2 0 0 0<1号更改为2>

// <询问[1,3],结果为2+0+0>

// 2 0 5 0 <3号更改为5>

// <询问[1,3]结果为2+0+5>

// 2 0 5 100<4号更改为100>

// <询问[1,3],结果为2+0+5>

#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    int n,m;
    cin >> n >> m;
    vector<int> ans, arr(n+1), ops(m), L(m), R(m);
    vector<ll> tree(n+1);
    for (int i = 0; i < m; i++) cin >> ops[i];
    for (int i = 0; i < m; i++) cin >> L[i];
    for (int i = 0; i < m; i++) cin >> R[i];
    function<void(int,int)> update = [&] (int p, int delta) {
        while (p <= n)
        {
            tree[p] += delta;
            p += (p&-p);
        }
        return;
    };
    function<ll(int)> query = [&] (int p){
        ll s = 0;
        while (p)
        {
            s += tree[p];
            p -= (p&-p);
        }
        return s;
    };
    for (int i = 0; i < m; i++){
        if (ops[i] == 0) {
            int p = L[i];
            int delta = R[i]-arr[p];
            update(p,delta);
            arr[p] += delta;
        }
        else{
            int l = L[i], r = R[i];
            ans.push_back(query(r)-query(l-1));
        }
    }
    int sz = ans.size();
    for (int i = 0; i < sz; i++){
        cout << ans[i];
        if (i < n-1) cout << " ";
        else cout << '\n';
    }
    return 0;
}