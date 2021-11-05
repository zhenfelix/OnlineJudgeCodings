// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 1e5 + 10;
const int maxm = 1e7 + 10;

int n;
int arr[maxn], tmp[maxn];

ll merge(int left, int right)
{
    if (left == right)
        return 0;
    int mid = (left + right) / 2;
    ll sums = 0;
    sums += merge(left, mid);
    sums += merge(mid + 1, right);
    for (int i = left, j = mid + 1, k = left; i <= mid || j <= right;)
    {
        if (j > right || (i <= mid && arr[i] <= arr[j]))
        {
            sums += (ll)arr[i] * (right - j + 1);
            tmp[k++] = arr[i++];
        }
        else
        {
            tmp[k++] = arr[j++];
        }
    }
    for (int k = left; k <= right; k++)
        arr[k] = tmp[k];
    return sums;
}

void solve()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    ll res = merge(0, n - 1);
    printf("%ld\n", res);
}

int main()
{
    // freopen("input", "r", stdin);
    solve();
}
