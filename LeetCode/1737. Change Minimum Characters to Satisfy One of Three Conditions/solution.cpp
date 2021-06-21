class Solution {
public:
    int minCharacters(string a, string b) {
        vector<int> posta(26,0), prea(26,0), postb(26,0), preb(26,0);
        int n = a.size(), m = b.size();
        for (int i = 0; i < n; i++){
            posta[a[i]-'a']++;
            prea[a[i]-'a']++;
        }
        for (int i = 0; i < m; i++){
            postb[b[i]-'a']++;
            preb[b[i]-'a']++;
        }
        int res = n+m;
        for (int i = 0; i < 26; i++){
            res = min(res, n-prea[i]+m-preb[i]);
        }
        for (int i = 1; i < 26; i++){
            prea[i] += prea[i-1];
            preb[i] += preb[i-1];
        }
        for (int i = 24; i >= 0; i--){
            posta[i] += posta[i+1];
            postb[i] += postb[i+1];
        }
        for (int i = 1; i < 26; i++){
            res = min(res, prea[i-1]+postb[i]);
            res = min(res, preb[i-1]+posta[i]);
        }
        return res;
    }
};