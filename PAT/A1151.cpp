#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <unordered_set>
#include <algorithm>
//#include <pair>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* BuildTree(vector<int> &a, vector<int> &pre, int i, int j, int k, int l){
    if(i>j||k>l)return NULL;
    int val=pre[k],idx;
    TreeNode *root=new TreeNode(val);
    for(idx=i;idx<=j;idx++)if(a[idx]==val)break;
    root->left=BuildTree(a, pre, i, idx-1, k+1, k+idx-i);
    root->right=BuildTree(a, pre, idx+1, j, k+idx-i+1, l);
    return root;
}

//void preorder(TreeNode *root){
//    if(!root)return;
//    cout<<root->val<<" ";
//    preorder(root->left);
//    preorder(root->right);
//    return;
//}

TreeNode* LCA(TreeNode *root, int u, int v){
    if(!root)return root;
    if(root->val==u||root->val==v)return root;
    
    TreeNode *left=LCA(root->left, u, v);
    TreeNode *right=LCA(root->right, u, v);
    if(left&&right)return root;
    if(left)return left;
    return right;
}

int main()
{
//    freopen("input.txt","r",stdin);
    int n,m;
    cin>>m>>n;
    vector<int> a(n),pre(n);
    unordered_set<int> mp;
    for(int i=0;i<n;i++)cin>>a[i];
    for(int i=0;i<n;i++)cin>>pre[i];
    for(int i=0;i<n;i++)mp.insert(pre[i]);
    TreeNode *root=BuildTree(a, pre, 0, n-1, 0, n-1);
//    preorder(root);
    while (m--) {
        int u,v;
        cin>>u>>v;
        if(mp.find(u)==mp.end()){
            if(mp.find(v)==mp.end())cout<<"ERROR: "<<u<<" and "<<v<<" are not found."<<endl;
            else cout<<"ERROR: "<<u<<" is not found."<<endl;
        }
        else if(mp.find(v)==mp.end())cout<<"ERROR: "<<v<<" is not found."<<endl;
        else{
            TreeNode *anchor=LCA(root, u, v);
            if(anchor->val==u)cout<<u<<" is an ancestor of "<<v<<"."<<endl;
            else if(anchor->val==v)cout<<v<<" is an ancestor of "<<u<<"."<<endl;
            else cout<<"LCA of "<<u<<" and "<<v<<" is "<<anchor->val<<"."<<endl;
        }
        
    }
    
    return 0;
}

