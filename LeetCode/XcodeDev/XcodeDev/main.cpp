//
//  main.cpp
//  XcodeDev
//
//  Created by Zhen Fei on 3/6/21.
//  Copyright © 2021 zhenfisher. All rights reserved.
//

#include <stdio.h>
#include<unordered_map>
#include<queue>

using namespace std;

#define null -1000000000

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution
{
public:
    void dfs(TreeNode *root, int target, int presum, unordered_map<int, int> &cnt, int &res)
    {
        if (!root)
            return;
        presum += root->val;
        res += cnt[presum - target];
        cnt[presum] += 1;
        dfs(root->left, target, presum, cnt, res);
        dfs(root->right, target, presum, cnt, res);
        cnt[presum] -= 1;
        return;
    }

    int pathSum(TreeNode *root, int sum)
    {
        if (!root)
            return 0;
        int res = 0;
        unordered_map<int, int> cnt;
        cnt[0] = 1;
        dfs(root, sum, 0, cnt, res);
        return res;
    }
};

class Codec
{
public:
    // Decodes your encoded data to tree.
    TreeNode *deserialize(vector<int> data)
    {
        queue<TreeNode *> q;
        TreeNode *root = nullptr;
        int i = 0;
        if (data[0] > null)
        {
            root = new TreeNode(data[0]);
            q.push(root);
        }
        i++;
        while (i < data.size())
        {
            TreeNode *tmp = q.front();
            q.pop();
            
            if(i<data.size()&&data[i]>null){
                tmp->left = new TreeNode(data[i]);
                q.push(tmp->left);
            }
            i++;
            if (i < data.size() && data[i] > null){
                tmp->right = new TreeNode(data[i]);
                q.push(tmp->right);
            }
            i++;
        }
        return root;
    }
};


int main(){
    Codec cdc;
    vector<int> tmp {1, -2, -3, 1, 3, -2, null, -1};
    TreeNode *root = cdc.deserialize(tmp);
    Solution sol;
    printf("%d", sol.pathSum(root, -1));
    return 0;
}
