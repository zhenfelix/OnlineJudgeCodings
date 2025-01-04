#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> findProductsOfElements(vector<vector<long long>>& queries) {
        vector<int> ans;

        constexpr int mx = 50;

        auto calc = [](long long t) {
            long long cnt = 0;
            vector<long long> cc(mx,0);
            for (int i = mx - 1; i >= 0; --i) {
                int flag = (t >> i) & 1;
                long long b = (1LL << i);
                cc[i] += cnt * b;
                cc[i] += flag * (1 + (t & (b - 1)));
                cnt <<= 1;
                cnt |= flag;
            }
            long long sum = 0;
            for (auto& v : cc) {
                sum += v;
            }
            return make_pair(sum, cc);
        };

        auto check = [&](long long c) {
            if (c == 0) return vector<long long>(mx,0);
            long long lo = 0, hi = (1LL << mx);
            while (lo <= hi) {
                long long m = (lo + hi) / 2;
                auto [s, cc] = calc(m);
                if (s >= c) hi = m - 1;
                else lo = m + 1;
            }
            auto [s, cc] = calc(hi);
            for (int i = 0; i < mx; ++i) {
                if (s >= c) break;
                if ((lo >> i) & 1) {
                    s += 1;
                    cc[i] += 1;
                }
            }
            return cc;
        };

        auto quickmul = [&](long long a, long long q, long long m) {
            long long res = 1;
            a %= m;
            while (q) {
                if (q & 1) res = (res * a) % m;
                a = (a * a) % m;
                q >>= 1;
            }
            return res;
        };

        for (auto& query : queries) {
            long long start = query[0], end = query[1], mod = query[2];
            auto cc2 = check(end + 1);
            auto cc1 = check(start);
            long long cur = 1;
            for (int i = 0; i < mx; ++i) {
                cur = (cur * quickmul(1LL << i, cc2[i] - cc1[i], mod)) % mod;
            }
            ans.push_back(static_cast<int>(cur));
        }

        return ans;
    }
};