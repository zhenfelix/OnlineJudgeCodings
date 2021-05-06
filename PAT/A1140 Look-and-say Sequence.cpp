#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

string nextNum(string &cur){
    int n = cur.size();
    string nxt;
    for (int i = 0; i < n;){
        int cnt = 1;
        while (i+1 < n && cur[i] == cur[i+1]){
            cnt++;
            i++;
        }
            
        nxt.push_back(cur[i++]);
        string tmp = std::to_string(cnt);
        for (auto ch : tmp)
            nxt.push_back(ch);
    }
    return nxt;
}

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);
    int d, n;
    cin >> d >> n;
    string cur = std::to_string(d);
    n--;
    while(n--){
        cur = nextNum(cur);
    }
    cout << cur << endl;
    return 0;
}
