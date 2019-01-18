iteration version
```c++
class Solution {
public:
    string countAndSay(int n) {
        string s = "1";
        for (int i = 1; i < n; i++) {
            char c = s[0];
            int cnt = 1;
            string new_s;
            for (int j = 1; j < s.size(); j++) {
                if (s[j] == s[j - 1]) {
                    cnt++;
                }
                else {
                    new_s += to_string(cnt) + c;
                    c = s[j];
                    cnt = 1;
                }
            }
            new_s += to_string(cnt) + c;
            s = new_s;
        }
        return s;
    }
};
```
