
# 小红书春招-2023.03.26-第三题-涂色
# 题目内容

# 给出一个数组，你需要求出按顺序对其进行一系区间操作后终所得的数组。

# 操作有三种

# 1.将下标在L到R之间的元素全部或上X。

# 2.将下标在L到R之间的元素全部与上X。

# 3.将下标在L到R之间的元素全部设为X。
# 输入描述

# 第一行有一个正整数 N(1⩽N⩽100000)N(1⩽N⩽100000)，代表数组的长度。

# 第二行有 NN 个非负整数，范围在00到 220−1220−1之间，代表数组中的元素。

# 第三行有一个正整数M（1⩽M⩽1000001⩽M⩽100000），代表操作次数。

# 第四行有M个正整数，代表M次操作中的区间左端点L。

# 第五行有M个正整数，代表M次操作中的区间右通点R。

# 第六行是一个长度为M的字符串，'|' 代表操作1，'&' 代表操作2。'=' 代表操作3。

# 第七行有M个正整数，代表M次操作中的参数X.
# 输出描述

# 在一行中输出N个数，代表所有操作按顺序完成后最终所得的数据。
# 样例

# 输入

# 4
# 5 4 7 4
# 4
# 1 2 3 2
# 4 3 4 2
# =|&=
# 8 3 6 2

# 输出

# 8 2 2 0


#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())
#define ln '\n'
typedef pair<int,int> pii;

const int N=1e5+5;
const int inf=1e8;

int n,m;
int arr[N], leftq[N], rightq[N], values[N], mp[N*2];
char ops[N];

vector<pii> push[N], pop[N];
bool inqueue[N*2];

void solve() {
    int bmax = 21;
    int ans[n] = {0};

    for (int b = 0; b < bmax; b++) {
        for (int i = 0; i < n+m; i++) inqueue[i] = false;
        priority_queue<pii, vector<pii>, greater<>> hq;
        for (int i = 0; i < n+1; i++){
            push[i].clear();
            pop[i].clear();
        }
        for (int i = 0; i < n; i++) {
            int v = (arr[i]>>b)&1;
            push[i].pb({inf, i});
            pop[i+1].pb({inf, i});
            mp[i] = v;
        }

        for (int i = 0; i < m; i++) {
            int l = leftq[i]-1, r = rightq[i]-1, v = values[i];
            if ((ops[i] == '=' && ((v>>b)&1)) || (ops[i] == '|' && ((v>>b)&1))) {
                push[l].pb({-i, i+n});
                pop[r+1].pb({-i, i+n});
                mp[i+n] = 1;
            }
            else if ((ops[i] == '=' && ((v>>b)&1) == 0) || (ops[i] == '&' && ((v>>b)&1) == 0)) {
                push[l].pb({-i, i+n});
                pop[r+1].pb({-i, i+n});
                mp[i+n] = 0;
            }
        }

        for (int i = 0; i < n; i++) {
            for (auto& [t, j] : push[i]) {
                hq.push({t,j});
                inqueue[j] = true;
            }
            for (auto& [t, j] : pop[i]) {
                inqueue[j] = false;
            }
            while (!hq.empty() && !inqueue[hq.top().second])
                {
                    hq.pop();
                }

            int v = 0;
            if (!hq.empty() && (mp[hq.top().second]))
            {
                v = 1;
            }
            if (v) ans[i] |= (1<<b);
        }
    }
    for (int i = 0; i < n; i++) {
        cout << ans[i] << " ";
    }
    cout << ln;
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
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        cin >> m;
        for (int i = 0; i < m; i++) cin >> leftq[i];
        for (int i = 0; i < m; i++) cin >> rightq[i];
        for (int i = 0; i < m; i++)
            cin >> ops[i];
        for (int i = 0; i < m; i++)
            cin >> values[i];
        solve();
    }
    return 0;
}
