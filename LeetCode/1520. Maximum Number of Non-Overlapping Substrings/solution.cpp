using ppp = tuple<int,int,int>;
using pp = pair<int,int>;

class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        int sn = s.length();
        vector<int> lo(26,sn), hi(26,-1);
        for (int i = 0; i < sn; i++){
            int ch = s[i]-'a';
            lo[ch] = min(lo[ch],i);
            hi[ch] = max(hi[ch],i);
        }
        vector<pp> intervals;
        for (int i = 0; i < 26; i++)
            intervals.push_back({lo[i],hi[i]});
        vector<vector<bool>> graph(26,vector<bool>(26,false));
        for (int i = 0; i < sn; i++){
            int ch = s[i]-'a';
            for (int j = 0; j < 26; j++){
                if (ch == j)
                    continue;
                auto [l,r] = intervals[j];
                if (l < i && i < r)
                    graph[j][ch] = true;
            }
        }
        for (int k = 0; k < 26; k++){
            for (int i = 0; i < 26; i++){
            for (int j = i+1; j < 26; j++){
                if (graph[i][j] && graph[j][i]){
                    auto [li,ri] = intervals[i];
                    auto [lj,rj] = intervals[j];
                    int l = min(li,lj);
                    int r = max(ri,rj);
                    intervals[i] = {l,r};
                    intervals[j] = {l,r};
                }
            }
        }
        }
        sort(intervals.begin(), intervals.end());
        int n = intervals.size();
        vector<pp> st = {{-1,-1}};
        for (int i = 0; i < n; i++){
            auto [l,r] = st.back();
            auto [ll,rr] = intervals[i];
            // cout << ll << " " << rr << endl;
            if (ll >= sn)
                break;
            if (l <= ll && rr <= r)
                st.pop_back();
            st.push_back({ll,rr});

        }
        vector<string> ans;
        for (auto [l,r] : st){
            if (l >= 0)
                ans.push_back(s.substr(l,r-l+1));
        }
        return ans;
    }
};