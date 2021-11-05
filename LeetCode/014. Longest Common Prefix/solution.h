class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        int n = strs.size();
        for (int cur = 0;;cur++){
            for (int i = 0; i < n; i++){
                if (cur == strs[i].length() || (i && strs[i][cur] != strs[i-1][cur]))
                    return res;
            }
            res.push_back(strs[0][cur]);
        }
    }
};









#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans="";
        int idx=0;
        if(strs.size()==0)return ans;
        while(1){
            char tmp=strs[0][idx];
            for(int i=0;i<strs.size();i++){
                if(strs[i][idx]!=tmp||idx>=strs[i].size())return ans;
            }
            ans+=strs[0][idx];
            idx++;
        }
    }
};
