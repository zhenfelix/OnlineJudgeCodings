class Solution {
public:
    int secondHighest(string s) {
        set<int> st;
        for (char c : s)
            if ('0' <= c && c <= '9')
                st.insert(c - '0');
        vector<int> v(st.begin(), st.end());
        if (v.size() < 2)
            return -1;
        return v[v.size() - 2];
    }
};