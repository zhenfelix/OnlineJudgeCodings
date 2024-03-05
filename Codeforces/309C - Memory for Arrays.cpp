/**
 * Created by 5cm/s on 2024/01/25 11:08:08.
 * 诸天神佛，佑我上分！
 **/
#include <bits/stdc++.h>

using namespace std;

#define itr(it) begin(it), end(it)
#define endl '\n'
#define YES() void(cout << "YES\n")
#define NO() void(cout << "NO\n")

using i64 = int64_t;

void elysia() {
    int n, m;
    cin >> n >> m;
    vector<int> a(30), b(30);
    for (int i = 0, x; i < n; ++i) {
        cin >> x;
        while (x) a[__lg(x & -x)]++, x &= x - 1;
    }
    for (int i = 0, x; i < m; ++i) {
        cin >> x;
        b[x]++;
    }
    int ok = 1;
    for (int i = 0; i < 30 && ok; ++i) {
        while (ok && b[i]) {
            int j = find_if(a.begin() + i, a.end(), [&](int x) { return x > 0; }) - a.begin();
            if (j < 30) while (j > i) a[j - 1] += 2, a[j]--, j--;
            if (!a[i]) ok = 0;
            else a[i]--, b[i]--;
        }
    }
    cout << m - accumulate(itr(b), 0) << endl;
}

int main() {
#ifdef MEGURINE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    clock_t start = clock();
#endif
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int T = 1;
//    cin >> T;
    cout << fixed << setprecision(12);
    while (T--) elysia();
#ifdef MEGURINE
    cout << "\nRunning Time: " << double(clock() - start) / CLOCKS_PER_SEC * 1000 << "ms" << endl;
#endif
    return 0;
}