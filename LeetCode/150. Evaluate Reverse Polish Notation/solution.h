class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> nums;
        for(auto str: tokens){
            if(str=="+"){
                int b=nums.top();nums.pop();
                int a=nums.top();nums.pop();
                nums.push(a+b);
            }
            else if(str=="-"){
                int b=nums.top();nums.pop();
                int a=nums.top();nums.pop();
                nums.push(a-b);
            }
            else if(str=="*"){
                int b=nums.top();nums.pop();
                int a=nums.top();nums.pop();
                nums.push(a*b);
            }
            else if(str=="/"){
                int b=nums.top();nums.pop();
                int a=nums.top();nums.pop();
                nums.push(a/b);
            }
            else nums.push(stoi(str));
        }
        return nums.top();
    }
};