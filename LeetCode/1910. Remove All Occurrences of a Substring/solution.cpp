class Solution {
public:
    string removeOccurrences(string s, string part) {
        string ans;
        for (char c : s) {
            ans.push_back(c);
            if (ans.size() >= part.size() && ans.substr(ans.size() - part.size(), part.size()) == part)
                ans = ans.substr(0, ans.size() - part.size());
        }
        return ans;
    }
};
