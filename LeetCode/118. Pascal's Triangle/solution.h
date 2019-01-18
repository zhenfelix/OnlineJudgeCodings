#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        for(int i=0;i<numRows;i++){
            vector<int> tmp;
            for(int j=0;j<i+1;j++){
                if(j==0||j==i){
                    tmp.push_back(1);
                    continue;
                }
                int t=ans[i-1][j-1]+ans[i-1][j];
                tmp.push_back(t);
            }
            ans.push_back(tmp);
        }
        return ans;
    }
};
