#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

bool isPrime(int x){
    for (int i = 2; i <= sqrt(x); i++){
        if (x%i == 0)
            return false;
    }
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int n, i = 0;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end(), greater<int>());
    for(; arr[i] > i+1; i++);
    cout << i << endl;
    return 0;
}
