#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

bool isPrime(int x)
{
     if (x <= 1) return false;
    int Sqrt = sqrt(x);
    for (int i = 2; i <= Sqrt; i++)
    {
         if (x % i == 0) return false;
    }
    return true;
}
int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);
    int mSize, n, m, x;
    cin >> mSize >> n >> m;
    while (!isPrime(mSize))
        mSize++;
    vector<int> hashTable(mSize, 0);
    for (int i = 0; i < n; i++)
    {
         cin >> x;
        bool flag = false;
        if (hashTable[x % mSize] == 0)
        {
             hashTable[x % mSize] = x;
            continue;
        }
        for (int step = 1; step < mSize; step++)
        {
             if (hashTable[(x + step * step) % mSize] == 0)
            {
                 hashTable[(x + step * step) % mSize] = x;
                flag = true;
                break;
            }
        }
        if (flag == false)
            cout << x << " cannot be inserted.\n";
    }
    double ans = 0.0;
    for (int i = 0; i < m; i++)
    {
         cin >> x;
        for (int step = 0; step <= mSize; step++)
        {
             ans++;
            if (hashTable[(x + step * step) % mSize] == x || hashTable[(x + step * step) % mSize] == 0)
                break;
        }
    }
    // printf("%.1f", ans / m);
    cout << ans/m << endl;
    return 0;
}
