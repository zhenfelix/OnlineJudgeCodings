#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    void dfs(TreeNode *root, int &ans, int level){
        if(root==NULL)return;
        level++;
        if(level>ans)ans=level;
        dfs(root->left,ans,level);
        dfs(root->right,ans,level);
        return;
    }
    int maxDepth(TreeNode* root) {
        int ans=0;
        dfs(root,ans,0);
        return ans;
    }
};
