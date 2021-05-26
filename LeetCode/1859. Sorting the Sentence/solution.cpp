#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string res[20] = {};
    string sortSentence(string s) {
        stringstream sin(s);
        string str;
        while (sin >> str) {
            int len = (int)str.size();
            int num = str[len - 1] - '0';
            res[num] = str.substr(0, len - 1);
        }

        string ans = "";
        for (int i = 0; i < 20; i++) {
            if (res[i] == "")
                continue;
            if ((int)ans.size() > 0)
                ans.append(" ");
            ans.append(res[i]);
        }
