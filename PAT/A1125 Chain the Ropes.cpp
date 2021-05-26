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
    int n;
    cin >> n;
    priority_queue<double, vector<double>, greater<double>> pq;

    for (int i = 0; i < n; i++){
        double x;
        cin >> x;
        pq.push(x);
    }
    double res = 0;
    while (pq.size() > 1)
    {
        double a = pq.top(); pq.pop();
        double b = pq.top(); pq.pop();
        pq.push((a + b)/2);
    }
    cout << (int) pq.top() << endl;
    
    
   
    
    return 0;
}
