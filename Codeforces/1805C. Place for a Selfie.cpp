/**
 * Created by megurine on 2023/04/02 22:48:18.
 * 诸天神佛，佑我上分！
 **/
#include <bits/stdc++.h>

using namespace std;

#define itr(it) begin(it), end(it)
typedef long long ll;
typedef long double ld;
typedef pair<int, int> PII;
#define endl '\n'
#define YES() void(cout << "YES\n")
#define NO() void(cout << "NO\n")

template<typename T>
void chmax(T &a, T b) { if (b > a) a = b; }

template<typename T>
void chmin(T &a, T b) { if (b < a) a = b; }

void elysia() {
    int n, m;
    cin >> n >> m;
    vector<ll> p(n);
    for (ll &x: p) cin >> x;
    std::sort(p.begin(), p.end());
    for (int i = 0; i < m; ++i) {
        ll a, b, c;
        cin >> a >> b >> c;
        int j = upper_bound(itr(p), b) - p.begin();
        if (j < n && (b - p[j]) * (b - p[j]) < 4 * a * c) {
            YES();
            cout << p[j] << endl;
            continue;
        }
        if (j && (b - p[j - 1]) * (b - p[j - 1]) < 4 * a * c) {
            YES();
            cout << p[j - 1] << endl;
            continue;
        }
        NO();
    }
}

int main() {
#ifdef MEGURINE
#define fr(x) freopen(x, "r", stdin)
#define fw(x) freopen(x, "w", stdout)
    fr("../input.txt");
    fw("../output.txt");
    clock_t start = clock();
#endif
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int T = 1;
    cin >> T;
    cout << fixed << setprecision(12);
    while (T--) {
        elysia();
    }
    cout.flush();
#ifdef MEGURINE
    clock_t end = clock();
    cout << "\n\nRunning Time : " << (double) (end - start) / CLOCKS_PER_SEC * 1000 << "ms" << endl;
#endif
    return 0;
}