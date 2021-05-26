class Solution {
public:
    bool checkZeroOnes(string s) {
        int n = s.size();
        vector<int> a(2);
        for (int i = 0, j; i < n; i = j) {
            for (j = i + 1; j < n && s[j] == s[i]; ++j);
            int x = s[i] - '0';
            a[x] = max(a[x], j - i);
        }
        return a[1] > a[0];
    }
};


class Solution {
public:
    bool checkZeroOnes(string s) {
        int mx1=0, mx0=0;
        int cur1=0, cur0=0;
        for (char c: s) {
            if (c=='1') {
                cur1++;
                cur0=0;
            } else {
                cur1=0;
                cur0++;
            }
            mx1=max(mx1, cur1);
            mx0=max(mx0, cur0);
        }
        return mx1>mx0;
    }
};