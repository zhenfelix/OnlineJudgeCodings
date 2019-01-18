#include <vector>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;


class Solution {
public:
    string int2string(int x){
        stack<int> t;
        string ans;
        char base='0';
        while(x!=0){
            t.push(x%10);
            x=x/10;
        }
        while(!t.empty()){
            base+=t.top();
            ans=ans+base;
            base='0';
            t.pop();
        }
        return ans;
    }
    vector<string> fizzBuzz(int n) {
        vector<string> ans;
        for(int i=1;i<=n;i++){
            string tmp;
            if(i%15==0)tmp="FizzBuzz";
            else if(i%5==0)tmp="Buzz";
            else if(i%3==0)tmp="Fizz";
            else tmp=int2string(i);
            ans.push_back(tmp);
        }
        return ans;
    }
};
