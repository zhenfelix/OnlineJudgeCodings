const int inf = 0x3f3f3f3f;
const int maxn = 1e5+10;
const int MOD = 1e9+7;
using ll = long long;

int cnt[maxn];


class Solution {
public:
    int minWastedSpace(vector<int>& packages, vector<vector<int>>& boxes) {
        memset(cnt, 0, maxn*sizeof(int));
        ll tot = 0;
        int n = packages.size();
        for (auto p : packages) cnt[p]++, tot += p;
        for (int i = 1; i < maxn; i++) cnt[i] += cnt[i-1];
        ll res = LONG_MAX;
        for (auto &box : boxes){
            sort(box.begin(), box.end());
            ll sums = 0, pre = 0, cur = 0;
            for (auto b : box){
                cur = cnt[b];
                sums += (cur-pre)*b;
                pre = cur;
                if (cur == n)
                    break;
            }
            if (cur < n)
                continue;
            res = min(res, sums-tot);
        }
        return res == LONG_MAX ? -1 : res%MOD;
    }
};


class Solution {
public:
    int minWastedSpace(vector<int>& A, vector<vector<int>>& boxes) {
        sort(A.begin(), A.end());
        long res = LONG_MAX, mod = 1e9 + 7, sumA = 0;
        // cout << res << endl;
        for (int a : A)
            sumA += a;
        for (auto& B : boxes) {
            sort(B.begin(), B.end());
            if (B[B.size() - 1] < A[A.size() - 1]) continue;
            long cur = 0, i = 0, j;
            for (int b : B) {
                j = upper_bound(A.begin(), A.end(), b) - A.begin();
                cur += b * (j - i);
                i = j;
            }
            res = min(res, cur);
        }
        return res < LONG_MAX ? (res - sumA) % mod : -1;
    }
};



// using ll = long long;

// class Solution {
// public:
//     int minWastedSpace(vector<int>& packages, vector<vector<int>>& boxes) {
//         const int MOD = 1e9+7;
//         const ll inf = 1e10+1;
//         sort(packages.begin(), packages.end());
//         vector<ll> presums = {0};
//         for (auto p : packages)
//             presums.push_back(presums.back()+p);
//         for (auto &box : boxes)
//             sort(box.begin(), box.end());
//         int n = boxes.size(), m = packages.size();
//         vector<ll> ans(n,0);
//         for (int i = 0; i < n; i++){
//             int pre = 0;
//             for (int j = 0; j < boxes[i].size(); j++){
//                 int cur = upper_bound(packages.begin(), packages.end(), boxes[i][j])-packages.begin();
//                 ans[i] += static_cast<ll>(boxes[i][j])*(cur-pre)-(presums[cur]-presums[pre]);
//                 pre = cur;
//             }
//             ans[i] = pre < m ? inf : ans[i];
//         }
//         ll res = *min_element(ans.begin(), ans.end());
//         return res < inf ? res%MOD : -1;
//     }
// };