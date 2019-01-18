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
