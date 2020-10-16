/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
const int N=50005;
#define rep(i,n) for(int i=1;i<=n;++i)
#define pb push_back
class Solution {
public:
    vector<int>g[N];
    bool is[N];
    int ans;
    void dfs(int x,int fa){
        if(g[x].size()==1)is[x]=1,++ans;
        for(int v:g[x])if(v!=fa)dfs(v,x);
        if(g[x].size()>2){
            if(is[x])--ans;
        }else is[fa]|=is[x];
    }
    int navigation(TreeNode* root) {
        TreeNode* a[N];
        int l=0,r=1;a[1]=root;
        ans=0;
        while(l<r){
            TreeNode* x=a[++l];
            if(x->left!=NULL)a[++r]=x->left;
            if(x->right!=NULL)a[++r]=x->right;
        }
        rep(i,r)g[i].clear();
        for(int i=1;i<=r;++i){
            TreeNode* x=a[i];
            if(x->left!=NULL)g[x->val].pb(x->left->val),g[x->left->val].pb(x->val);
            if(x->right!=NULL)g[x->val].pb(x->right->val),g[x->right->val].pb(x->val);
        }
        int rt=0;
        for(int i=1;i<=r;++i)if(g[i].size()>2)rt=i;
        if(rt==0)return 1;
        dfs(rt,0);
        return ans;
    }
};
