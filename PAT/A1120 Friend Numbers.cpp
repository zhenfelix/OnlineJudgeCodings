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
    int n, k;
    cin >> n;
    set<int> mp;
    vector<int> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
        int sums = 0;
        while (arr[i]){
            sums += arr[i]%10;
            arr[i] /= 10;
        }
        mp.insert(sums);
    }
    cout << mp.size() << endl;
    int cnt = 1;
    for (auto item : mp){
        if (cnt++ > 1)
            cout << " ";
        cout << item;
    }
    cout << endl;
    return 0;
}
