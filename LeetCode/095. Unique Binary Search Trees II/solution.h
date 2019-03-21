/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if(n==0)return {};
        return helper(1, n);
    }
    vector<TreeNode*> helper(int start, int end){
        if(start>end)return {NULL};
        vector<TreeNode*> ans;
        for(int v=start;v<=end;v++){
            vector<TreeNode*> left=helper(start,v-1);
            vector<TreeNode*> right=helper(v+1,end);
            for(auto l: left){
                for(auto r: right){
                    TreeNode* root=new TreeNode (v);
                    root->left=l;
                    root->right=r;
                    ans.push_back(root);
                }
            }
        }
        return ans;
    }
};