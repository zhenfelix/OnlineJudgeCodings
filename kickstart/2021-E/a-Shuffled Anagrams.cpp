1953. Maximum Number of Weeks for Which You Can Work

#include <bits/stdc++.h>

using namespace std;
const int inf = 0x3f3f3f3f;

class Solution
{
public:
    string anagram(string &s)
    {
        vector<int> cnt(26,0), idx(26), sums(26,0), sums_mp(26);
        int n = s.length();
        
        for (auto ch : s){
            cnt[ch-'a']++;
        }
        for (int i = 0; i < 26; i++)
            idx[i] = i;
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return cnt[a] > cnt[b];
        });
        if (cnt[idx[0]] > n-cnt[idx[0]])
            return "IMPOSSIBLE";
        sums[0] = cnt[idx[0]];
        for (int i = 1; i < 26; i++)
            sums[i] = cnt[idx[i]] + sums[i-1];
        for (int i = 0; i < 26; i++){
            sums_mp[idx[i]] = sums[i];
        }
        string res(n, '#');
        vector<int> arr(n);
        int a = 0, b = sums[0];
        for (int i = 0; i < n; i++){
            int j = s[i]-'a';
            arr[--sums_mp[j]] = i;
        }
        for(;a < n; a++, b++){
            res[arr[a]] = s[arr[b % n]];
        }
        return res;
    }
};

int main()
{
    // freopen("input", "r", stdin);
    Solution sol;
    int T, idx = 1;
    string s;
    cin >> T;
    while (T--)
    {
        cin >> s;
        cout << "Case #" << idx++ << ": " << sol.anagram(s) << endl;
    }
}



#include <bits/stdc++.h>
using namespace std;

void Main() {
  string S;
  cin >> S;
  map<char, int> cnt;
  for (auto i : S) cnt[i]++;
  int mx = 0;
  for (auto i : cnt) mx = max(mx, i.second);
  if (mx > int(S.size()) - mx) {
    cout << "IMPOSSIBLE\n";
    return;
  }
  int n = S.size();
  vector<pair<char, int>> pos;
  for (int i = 0; i < n; i++) {
    pos.emplace_back(S[i], i);
  }
  sort(begin(pos), end(pos));
  for (int i = 0; i < n; i++) {
    S[pos[(i + mx) % n].second] = pos[i].first;
  }
  cout << S << '\n';
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int T = 1;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    Main();
  }
  return 0;
}
