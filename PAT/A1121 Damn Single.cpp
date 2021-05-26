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
    int n, m;
    string a, b;
    
    map<string,string> couple;
    set<string> guests, res;
    cin >> n;
    while (n--)
    {
        cin >> a >> b;
        couple[a] = b;
        couple[b] = a;
    }
    cin >> m;
    while (m--)
    {
        cin >> a;
        guests.insert(a);
    }
    for (auto id : guests){
        if (couple.find(id) == couple.end() || guests.find(couple[id]) == guests.end())
            res.insert(id);
    }
    cout << res.size() << endl;
    int cnt = 1;
    for (auto id : res){
        if (cnt++ > 1)
            cout << " ";
        cout << id;
    }
    
    
    return 0;
}
