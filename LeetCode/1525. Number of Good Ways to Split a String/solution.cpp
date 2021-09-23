class Solution {
public:
    int numSplits(string s) {
        vector<int> left(26,0), right(26,0);
        int cnt_left = 0, cnt_right = 0, n = s.length(), res = 0;
        for (int i = 0; i < n; i++){
            int j = s[i]-'a';
            if (right[j] == 0)
                cnt_right++;
            right[j]++;
        }
        for (int i = 0; i < n-1; i++){
            int j = s[i]-'a';
            if (left[j] == 0)
                cnt_left++;
            left[j]++;
            right[j]--;
            if (right[j] == 0)
                cnt_right--;
            res += (cnt_right == cnt_left);
        }
        return res;
    }
};