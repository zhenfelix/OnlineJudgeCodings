class Solution {
public:
    bool closeStrings(string word1, string word2) {
        vector<int> cc1(26,0), cc2(26,0);
        int n = word1.size(), m = word2.size();
        if (n != m)
            return false;
        for (int i = 0; i < n; i++){
            cc1[word1[i]-'a']++;
            cc2[word2[i]-'a']++;
        }
        for (int i = 0; i < 26; i++)
            if ((cc1[i] != 0 && cc2[i] == 0) || (cc1[i] == 0 && cc2[i] != 0))
                return false;
        sort(cc1.begin(), cc1.end());
        sort(cc2.begin(), cc2.end());
        return cc1 == cc2;
    }
};