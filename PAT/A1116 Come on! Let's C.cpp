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
    string id;
    map<string,int> rank;
    set<string> checked;
    cin >> n;
    for (int i = 1; i <= n; i++){
        cin >> id;
        rank[id] = i;
    }
    cin >> k;
    while (k--) 
    {
        cin >> id;
        cout << id << ": ";
        
        if (rank.find(id) == rank.end()){
            cout << "Are you kidding?\n";
        }
        else if (checked.find(id) != checked.end())
        {
            cout << "Checked\n";
        }
        else if (rank[id] == 1){
            cout << "Mystery Award\n";
        }
        else if (isPrime(rank[id])){
            cout << "Minion\n";
        }
        else{
            cout << "Chocolate\n";
        }
        checked.insert(id);
    }

    // for (int i = 2; i < 100; i++){
    //     if (isPrime(i))
    //         cout << i << endl;
    // }
    
    return 0;
}
