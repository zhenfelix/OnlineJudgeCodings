// class Solution {
// public:

//     void dfs(set<string> &ans, int &len_max, string tmp, int left, int idx, string s){
//         if(tmp.length()+s.length()-idx < len_max)return;//pruning
//         if(idx==s.length()){
//             if(left==0 && tmp.length()>=len_max){
//                 if(tmp.length()>len_max){
//                     len_max=tmp.length();
//                     ans.clear();
//                 }
//                 ans.insert(tmp);
//             }
//             return;
//         }
//         if(s.substr(idx,1)!="(" && s.substr(idx,1)!=")"){
//             dfs(ans,len_max,tmp+s.substr(idx,1),left,idx+1,s);
//         }
//         else if(left>=0){//pruning
            
//             if(s.substr(idx,1)=="("){
//                 dfs(ans,len_max,tmp+s.substr(idx,1),left+1,idx+1,s);
//             }
//             else{
//                 dfs(ans,len_max,tmp+s.substr(idx,1),left-1,idx+1,s);
//             }
//             dfs(ans,len_max,tmp,left,idx+1,s);
//         }
//         return;
//     }
//     vector<string> removeInvalidParentheses(string s) {
//         vector<string> ans;
//         set<string> ans_;
//         string tmp="";
//         int len_max=0;
//         dfs(ans_,len_max,tmp,0,0,s);
//         for(auto str: ans_)ans.push_back(str);
//         return ans;
//     }
// };


class Solution {
public:

    void dfs(set<string> &ans, string tmp, int left_cc, int left_remain, int right_remain, int idx, string s){
        if(idx==s.length()){
            if(left_remain==0 && right_remain==0){
                ans.insert(tmp);
            }
            return;
        }
        if(s.substr(idx,1)!="(" && s.substr(idx,1)!=")"){
            dfs(ans,tmp+s.substr(idx,1),left_cc,left_remain,right_remain,idx+1,s);
        }
        else{
            if(s.substr(idx,1)=="("){
                if(left_remain>0)dfs(ans,tmp,left_cc,left_remain-1,right_remain,idx+1,s);
                dfs(ans,tmp+s.substr(idx,1),left_cc+1,left_remain,right_remain,idx+1,s);
            }

            else{
                if(right_remain>0)dfs(ans,tmp,left_cc,left_remain,right_remain-1,idx+1,s);
                if(left_cc>0)dfs(ans,tmp+s.substr(idx,1),left_cc-1,left_remain,right_remain,idx+1,s);
            }
        }
        return;
    }
    vector<string> removeInvalidParentheses(string s) {
        vector<string> ans;
        set<string> ans_;
        string tmp="";
        int left=0,right=0;
        for(auto ch: s){
            if(ch=='(')left++;
            else if(ch==')'){
                if(left>0)left--;
                else right++;
            }
            else continue;
        }
        dfs(ans_,tmp,0,left,right,0,s);
        for(auto str: ans_)ans.push_back(str);
        return ans;
    }
};
