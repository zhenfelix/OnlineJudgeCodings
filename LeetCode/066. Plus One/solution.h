#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int a=1;
        vector<int> ans;
        for(int i=digits.size()-1;i>=0;i--){
            int tmp=a+digits[i];
            if(tmp>=10){
                ans.push_back(0);
                a=1;
                if(i==0)ans.push_back(1);
            }
            else {
                ans.push_back(tmp);
                a=0;
            }
        }
        for(int i=0;i<ans.size()/2;i++){
            int tmp=ans[i];
            ans[i]=ans[ans.size()-1-i];
            ans[ans.size()-1-i]=tmp;
        }
        return ans;
    }
};
