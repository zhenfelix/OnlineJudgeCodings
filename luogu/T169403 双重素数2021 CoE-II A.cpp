// #include <deque>
// #include <fstream>
// #include <iostream>
// #include <string>
// #include <cstring>
// #include <vector>
// #include <queue>
// #include <list>
// #include <algorithm>
// #include <numeric>
// #include <unordered_map>
// #include <iterator>
// #include <memory>

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 100000010;
const int inf = 0x3f3f3f3f;
int cnt = 0;

vector<int> dp, primes_small;
vector<bool> prime(maxn, true);

bool isDoublePrime(int x){
    int sums = 0;
    while (x){
        sums += (x%10);
        x /= 10;
    }
    for (const int &b : primes_small)
        if (b == sums)
            return true;
    return false;
}

void calc(){
    prime[0] = prime[1] = false;
    for (int i = 2; i < maxn; i++){
        if (prime[i])
            dp.push_back(i);
        if (prime[i] && (long long)i * i < maxn)
        {
            for (int j = i*i; j < maxn; j += i){
                prime[j] = false;
            }
        }
    }
    for (int i = 0; i < 30; i++)
        primes_small.push_back(dp[i]);
    
    for (int i = 0; i < dp.size(); i++){
        if (isDoublePrime(dp[i]))
            dp[cnt++] = dp[i];
    }
    return;
}


int main()
{
    calc();
    int T, L, R;
    cin >> T;
    while (T--){
        cin >> L >> R;
        cout << upper_bound(dp.begin(), dp.begin()+cnt, R) - lower_bound(dp.begin(), dp.begin()+cnt, L) << '\n';
    }
}