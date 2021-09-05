class Solution {
public:
    int countPalindromicSubsequence(string s) {
        std::vector<int> right(26,0), left(26,0);
        for (auto ch : s)
            right[ch-'a']++;
        vector<bool> seen(26*26,false);
        for (auto ch : s){
            int j = ch-'a';
            right[j]--;
            for (int i = 0; i < 26; i++)
                if (left[i] && right[i])
                    seen[i*26+j] = true;
            left[j]++;
        }
        int res = 0;
        for (auto x : seen)
            res += x;
        return res;
    }
};