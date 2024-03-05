// 问题描述

// 大风起兮云飞扬。威加海内兮归故乡。安得猛士兮守四方！

// 小蓝站在家乡的山上，感受着来自于西西伯利亚的风，回忆着汉楚那悲壮的历史。

// 突然，一排气球引起了小蓝的注意。山崖上有一排栅栏，每个栅栏上都绑上了一个气球，我们可以按照从左到右的顺序给每个气球编号 1∼n1∼n，每个气球上都有一个数字 pipi​。

// 小蓝知道，那是古老的祭祀仪式，用来缅怀逝去的亲人，当每一个气球被风吹走时，就代表亲人随风去到了天堂。

// 小蓝是个善于思考的人，他想到了一个问题，当一个气球飞走后，剩下的气球中，中位数是多少？

// 具体来说，初始存在 nn 个气球，编号为 1∼n1∼n，每个气球有一个权值 pipi​，每一秒，会有一个编号为 xixi​ 的气球随风飘走，小蓝想知道每飘走一个气球，剩下的气球按照权值排序后，中位数是多少？

// 中位数：对于一个长度为 nn，并且已经排好序的序列 aa 来说，如果 nn 为奇数，那么中位数为 an+12a2n+1​​；如果 nn 为偶数，那么中位数为 an2+an2+122a2n​​+a2n​+1​​。
// 输入格式

// 第一行输入一个整数 nn，表示气球的数量。

// 第二行输入 nn 个整数 p1,p2,p3,...,pi,...pnp1​,p2​,p3​,...,pi​,...pn​，代表每个气球的权值。

// 第三行一个整数 qq，代表会有 qq 个气球飘走。

// 第四行输入 qq 个整数 x1,x2,...,xqx1​,x2​,...,xq​，代表第 ii 秒编号为 xixi​ 的气球会飘走。
// 输出格式

// 输出一行，包含 qq 个浮点数 a1,a2,a3,...,aqa1​,a2​,a3​,...,aq​，代表第 xixi​ 个气球飘走后，剩下的气球经过排序后，中位数是 aiai​。每个数保留一位小数，每两个数之间用一个空格隔开。
// 样例输入

// 6
// 1 8 3 4 6 2
// 3
// 2 4 3
// [copy]

// 样例输出

// 3.0 2.5 2.0
// [copy]

// 说明

//     第一秒后，第 22 个气球飘走，剩下的气球经过排序后：1,2,3,4,61,2,3,4,6。
//     第二秒后，第 44 个气球飘走，剩下的气球经过排序后：1,2,3,61,2,3,6。
//     第三秒后，第 33 个气球飘走，剩下的气球经过排序后：1,2,61,2,6。

// 评测数据范围

// 1≤q<n≤2×105,1≤pi≤109,1≤xi≤n1≤q<n≤2×105,1≤pi​≤109,1≤xi​≤n。

// 保证 xixi​ 各不相同。

// 数据量较大，请尽量使用较快的输入输出方式。
// 运行限制
// 语言  最大运行时间  最大运行内存
// C++     2s  512M
// C   2s  512M
// Java    3s  512M
// Python3     4s  512M
// PyPy3   4s  512M
// Go  4s  512M
// JavaScript  4s  512M


#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;
using f64 = double_t;
int main() {
  cin.tie(nullptr)->sync_with_stdio(0);
  int n;
  cin >> n;
  vector<int> p(n + 1);
  for (int i = 1; i <= n; i += 1) { cin >> p[i]; }
  multiset<int> ls, rs;
  auto t = p;
  sort(t.begin(), t.end());
  for (int i = 1; i <= n / 2; i += 1) { ls.insert(t[i]); }
  for (int i = n / 2 + 1; i <= n; i += 1) { rs.insert(t[i]); }
  int q;
  cin >> q;
  for (int i = 0; i < q; i += 1) {
    int x;
    cin >> x;
    if (ls.find(p[x]) != ls.end()) {
      ls.extract(p[x]);
      if (rs.size() >= ls.size() + 2) {
        ls.insert(*rs.begin());
        rs.erase(rs.begin());
      }
    } else {
      rs.extract(p[x]);
      if (ls.size() > rs.size()) {
        rs.insert(*ls.rbegin());
        ls.extract(*ls.rbegin());
      }
    }
    if (ls.size() == rs.size()) {
      int x = *ls.rbegin() + *rs.begin();
      cout << x / 2 << "."
           << "05"[x % 2] << " ";
    } else {
      cout << *rs.begin() << ".0 ";
    }
  }
}