
// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;


void solve()
{
    int n;
    scanf("%d\n", &n);
    // vector<vector<int>> mat(n, vector<int>(n));
    int lo = 1, hi = n*n;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if ((i+j)&1) printf("%d",lo++);
            else printf("%d",hi--);
            if (j < n-1) printf(" ");
            else printf("\n");
        }
    }
}

int main()
{
    // freopen("input", "r", stdin);
    solve();
}
