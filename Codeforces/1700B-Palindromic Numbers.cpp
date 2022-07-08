
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
const int maxn = 100005;

char arr[maxn];

void simple(int left, int right){
    for (int i = left; i <= right; i++){
        int tmp = arr[i]-'0';
        tmp = 9-tmp;
        arr[i] = '0'+tmp;
    }
}

void addone(int left, int right){
    int plus = 1;
    for (int i = right; i >= left; i--){
        int tmp = arr[i]-'0'+plus+1;
        plus = tmp/10;
        tmp %= 10;
        arr[i] = '0'+tmp;
    }
}

void solve()
{
    int n;
    scanf("%d%s\n", &n, &arr);
    simple(0,n-1);
    if (arr[0] == '0') addone(0,n-1);
    for (int i = 0; i < n; i++) printf("%c",arr[i]);
    printf("\n"); 
}

int main()
{
    // freopen("input", "r", stdin);
    int t;
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        solve();
    }
}
