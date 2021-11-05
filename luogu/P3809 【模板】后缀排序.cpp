#include <bits/stdc++.h>

using namespace std;
const int inf = 0x3f3f3f3f;
const int maxn = 1e6+10;
int rk[maxn], group[maxn], tmp[maxn], perm[maxn], cnt[maxn];

void suffix(string s){
    s.push_back('#');
    int n = s.length();
    int mx = 256;
    memset(cnt, 0, n * sizeof(int));
    for (int i = 0; i < n; i++) group[i] = s[i];
    for (int i = 0; i < n; i++) cnt[group[i]]++;
    for (int i = 1; i < mx; i++) cnt[i] += cnt[i-1];
    for (int i = n-1; i >= 0; i--) rk[i] = --cnt[group[i]];
    for (int i = 0; i < n; i++) perm[rk[i]] = i;
    for (int i = 0; i < n; i++) tmp[i] = group[i];
    group[perm[0]] = 0;
    for (int i = 1; i < n; i++) group[perm[i]] = group[perm[i-1]] + (tmp[perm[i]] == tmp[perm[i-1]] ? 0 : 1);

    // for (int i = 0; i < n; i++)
    //     cout << rk[i] << " ";
    // cout << endl;
    // for (int i= 0; i < n; i++) cout << perm[i]+1 << " ";
    // cout << endl;

    for (int sz = 1; sz < n; sz *= 2){
        for (int i = 0; i < n; i++) perm[i] = (perm[i]-sz+n)%n;
        memset(cnt, 0, n*sizeof(int));
        for (int i = 0; i < n; i++) cnt[group[i]]++;
        for (int i = 1; i < n; i++) cnt[i] += cnt[i-1];
        for (int i = n-1; i >= 0; i--) rk[perm[i]] = --cnt[group[perm[i]]];
        for (int i = 0; i < n; i++) perm[rk[i]] = i;
        for (int i = 0; i < n; i++) tmp[i] = group[i];
        group[perm[0]] = 0;
        for (int i = 1; i < n; i++)
            group[perm[i]] = group[perm[i - 1]] + ((tmp[perm[i]] == tmp[perm[i - 1]] && tmp[(perm[i] + sz) % n] == tmp[(perm[i - 1] + sz) % n]) ? 0 : 1);
    }
    for (int i= 1; i < n; i++) cout << perm[i]+1 << " ";
    cout << endl;
}



int main()
{
    // freopen("input", "r", stdin);
    string s;
    cin >> s;
    suffix(s);
}


// #include<iostream> 
// #include<vector>
// #include <string>

// using namespace std;

// vector<int> sort_cyclic_shifts(string const& s) {
//     int n = s.size();
//     const int alphabet = 256;
//     vector<int> p(n), c(n), cnt(max(alphabet, n), 0);
//     for (int i = 0; i < n; i++)
//         cnt[s[i]]++;
//     for (int i = 1; i < alphabet; i++)
//         cnt[i] += cnt[i-1];
//     for (int i = 0; i < n; i++)
//         p[--cnt[s[i]]] = i;
//     c[p[0]] = 0;
//     int classes = 1;
//     for (int i = 1; i < n; i++) {
//         if (s[p[i]] != s[p[i-1]])
//             classes++;
//         c[p[i]] = classes - 1;
//     }
//     vector<int> pn(n), cn(n);
//     for (int h = 0; (1 << h) < n; ++h) {
//         for (int i = 0; i < n; i++) {
//             pn[i] = p[i] - (1 << h);
//             if (pn[i] < 0)
//                 pn[i] += n;
//         }
//         fill(cnt.begin(), cnt.begin() + classes, 0);
//         for (int i = 0; i < n; i++)
//             cnt[c[pn[i]]]++;
//         for (int i = 1; i < classes; i++)
//             cnt[i] += cnt[i-1];
//         for (int i = n-1; i >= 0; i--)
//             p[--cnt[c[pn[i]]]] = pn[i];
//         cn[p[0]] = 0;
//         classes = 1;
//         for (int i = 1; i < n; i++) {
//             pair<int, int> cur = {c[p[i]], c[(p[i] + (1 << h)) % n]};
//             pair<int, int> prev = {c[p[i-1]], c[(p[i-1] + (1 << h)) % n]};
//             if (cur != prev)
//                 ++classes;
//             cn[p[i]] = classes - 1;
//         }
//         c.swap(cn);
//     }
//     return p;
// }

// vector<int> suffix_array_construction(string s) {
//     s += "$";
//     vector<int> sorted_shifts = sort_cyclic_shifts(s);
//     sorted_shifts.erase(sorted_shifts.begin());
//     return sorted_shifts;
// }

// int main(){
//     string s;
//     cin >> s;
//     vector<int> res = suffix_array_construction(s);
//     for (int i = 0; i < res.size(); i++){
//         if (i > 0)
//             cout << ' ';
//         cout << res[i]+1;
//     }
//     cout << endl;
// }