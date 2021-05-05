class Solution {
public:
    int getMinSwaps(string s, int k) {
        string t = s;
        for (int i = 0; i < k; ++i) {
            next_permutation(s.begin(), s.end());
        }
        //cout << t << " " << s << endl;
        int ret = 0, n = s.size();
        for (int i = 0; i < n; ++i) {
            if (s[i] == t[i]) continue;
            int j;
            for (j = i + 1; j < n && s[i] != t[j]; ++j);
            for (int k = j; k > i; --k) {
                swap(t[k], t[k - 1]);
                ++ret;
            }
        }
        return ret;
    }
};