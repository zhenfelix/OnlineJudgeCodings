#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int m, n, s;
    set<string> winners;
    string name;
    cin >> m >> n >> s;
    int cnt = 0;
    while (m--)
    {
        cin >> name;
        if (winners.find(name) == winners.end()){
            cnt++;
            if (cnt >= s && (cnt-s)%n == 0){
                cout << name << endl;
                winners.insert(name);
            }
        }     
    }
    if (winners.empty())
        cout << "Keep going..." << endl;
   
    
    return 0;
}
