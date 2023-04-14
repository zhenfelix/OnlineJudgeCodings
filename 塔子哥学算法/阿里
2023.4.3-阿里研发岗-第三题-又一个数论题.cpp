
// 2023.4.3-阿里研发岗-第三题-又一个数论题
// 题目内容

// 塔子哥是一名年轻的数学家，他一直对数学充满热情。有一天，他在研究数论时发现了一个有趣的问题：给定一个长度为 nn 的数组 aa，问有多少个子数组的乘积的因数个数 ≥k≥k。

// 塔子哥对这个问题非常感兴趣，因为它可以帮助他更好地了解因数的性质，但是现在研究出现了一些问题，他想请你帮忙解决一下这个问题，你能帮塔子哥解决这个问题吗？
// 输入描述

// 第一行为两个整数 nn 和 kk ，（ 1≤n≤2×1051≤n≤2×105 ，1≤k≤1091≤k≤109 ）。

// 第二行为 nn 个整数，第 ii 个数为 aiai​ ，（ 1≤ai≤2×1051≤ai​≤2×105 ）。
// 输出描述

// 输出为一个整数，表示有多少个子数组的乘积的因数个数 ≥k≥k。
// 样例1

// 输入

// 3 2
// 2 2 2

// 输出

// 6

// 样例2

// 输入

// 3 3
// 2 2 2

// 输出

// 3

// 建议:

// python选手使用pypy3提交获得更快的速度

//     ps:目前各大笔试平台只有牛客提供pypy3编译器，能够跟C++去比比赛。其他平台，遇到py被卡，基本只能自认倒霉。当然这种情况也只会出现在压轴题。


#include<bits/stdc++.h>

using namespace std;
using ll = long long;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  // freopen("contests/input","r",stdin);
  int n,k;
  cin >> n >> k;
  vector<int> arr(n);
  for (int i = 0; i < n; i++) cin >> arr[i];
  int j = 0;
  ll ans = 0, cur = 1;
  int mx = *max_element(arr.begin(),arr.end());
  vector<int> cnt(mx+1,0);
  function<void(int,int)> calc = [&] (int a, int flag) {
    for (int f = 2; f*f <= a; f++) {
      while (a%f == 0)
      {
        cur /= (cnt[f]+1);
        cnt[f] += flag;
        cur *= (cnt[f]+1);
        a /= f;
      }
    }
    if (a > 1){
      cur /= (cnt[a]+1);
      cnt[a] += flag;
      cur *= (cnt[a]+1);
    }
  };
  for (int i = 0; i < n; i++) {
    calc(arr[i],1);
    while (cur >= k) {
      calc(arr[j],-1);
      j++;
    }
    ans += j;
  }
  cout << ans << endl;
}