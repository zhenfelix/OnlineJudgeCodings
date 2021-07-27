/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// class Solution {
// public:
//     int helper(TreeNode* root,int sum,bool flag){
//         if(!root)return 0;
//         int tmp=sum-root->val==0?1:0;
//         if(flag)return tmp+helper(root->left,sum-root->val,flag)+helper(root->right,sum-root->val,flag);
//         else return tmp+helper(root->left,sum-root->val,!flag)+helper(root->right,sum-root->val,!flag)+helper(root->left,sum,flag)+helper(root->right,sum,flag);
//     }
//     int pathSum(TreeNode* root, int sum) {
        
//         return helper(root,sum,false);
//     }
// };


// class Solution {
//     public: int pathSum(TreeNode* root, int sum) {
//         if (!root) return 0;
//         return pathSumFrom(root, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
//     }
    
//     private: int pathSumFrom(TreeNode* node, int sum) {
//         if (!node) return 0;
//         return (node->val == sum ? 1 : 0) 
//             + pathSumFrom(node->left, sum - node->val) + pathSumFrom(node->right, sum - node->val);
//     }
// };

// Typical recursive DFS.
// Space: O(n) due to recursion.
// Time: O(n^2) in worst case (no branching); O(nlogn) in best case (balanced tree).
// for the worst case, aka, a sequence of nodes, 1->2->...->i->...->n-1->n,  for node i, pathSumFrom(i,sumx), sumx has a upper bound of i possibilities, In other words, you can think of the options for the beginning and ending node, like a two pointer. Therefore in total O(N^2). the same argument goes for a balanced tree.



// class Solution{
//     public: 
//     int helper(TreeNode* root, int cur, int sum, unordered_map<int, int> pre){
//         if(!root)return 0;
//         cur+=root->val;
//         int ans=pre[cur-sum];
//         pre[cur]++;
//         return ans+helper(root->left,cur,sum,pre)+helper(root->right,cur,sum,pre);
//     }
//     int pathSum(TreeNode* root, int sum){
//         unordered_map<int, int> pre;
//         pre[0]=1;
//         return helper(root,0,sum,pre);
//     }
// };


class Solution{
    public: 
    void helper(TreeNode* root, int cur, int sum, unordered_map<int, int> &pre, int &cnt){
        if(!root)return;
        cur+=root->val;
        cnt+=pre[cur-sum];
        pre[cur]++;
        helper(root->left,cur,sum,pre,cnt);
        helper(root->right,cur,sum,pre,cnt);
        pre[cur]--;
        return;
    }
    int pathSum(TreeNode* root, int sum){
        unordered_map<int, int> pre;
        int cnt=0;
        pre[0]=1;
        helper(root,0,sum,pre,cnt);
        return cnt;
    }
};



// class Solution {
// public:
//     void helper(TreeNode *root, int &ret, int pre, int sum, unordered_map<int, int>& prefix) {
//         if (!root)
//             return;
//         root->val += pre;
//         ret += (root->val == sum) + (prefix.count(root->val - sum) ? prefix[root->val - sum] : 0);
//         prefix[root->val]++;
//         helper(root->left, ret, root->val, sum, prefix);
//         helper(root->right, ret, root->val, sum, prefix);  
//         prefix[root->val]--;

//     }
    
    
//     int pathSum(TreeNode* root, int sum) {
//         unordered_map<int, int> prefix;
//         int ret = 0;
//         helper(root, ret, 0, sum, prefix);
        
//         return ret;
//     }
// };

//So the idea is similar as Two sum, using HashMap to store ( key : the prefix sum, value : how many ways get to this prefix sum) , and whenever reach a node, we check if prefix sum - target exists in hashmap or not, if it does, we added up the ways of prefix sum - target into res.
// For instance : in one path we have 1,2,-1,-1,2, then the prefix sum will be: 1, 3, 2, 1, 3, let's say we want to find target sum is 2, then we will have{2}, {1,2,-1}, {2,-1,-1,2} and {2}ways.

// I used global variable count, but obviously we can avoid global variable by passing the count from bottom up. The time complexity is O(n). This is my first post in discuss, open to any improvement or criticism. :)

// WARNING for the HashMap, you should use reference, otherwise, it will cost you a lot time and space


class Solution {
public:
    int dfs(TreeNode* root, int sum){
        if(!root)return 0;
        // sum -= root->val
        return (root->val == sum ? 1: 0) + dfs(root->left, sum-root->val) + dfs(root->right, sum-root->val);
    }
        
        
    int pathSum(TreeNode* root, int sum) {
        if(!root)return 0;
        // printf("%d %d %d\n",dfs(root,sum),root->val,sum);
        return dfs(root,sum) + pathSum(root->left,sum) + pathSum(root->right,sum);
        
    }
};


class Solution {
public:
    void dfs(TreeNode* root, int target, int presum, unordered_map<int,int> &cnt, int &res){
        if(!root)return;
        presum += root->val;
        res += cnt[presum-target];
        cnt[presum]++;
        dfs(root->left,target,presum,cnt,res);
        dfs(root->right,target,presum,cnt,res);
        cnt[presum]--;
        return;
        }
        
        
    int pathSum(TreeNode* root, int sum) {
        if(!root)return 0;
        int res = 0;
        unordered_map<int,int> cnt;
        cnt[0] = 1;
        dfs(root,sum,0,cnt,res);
        return res;
        
    }
};


class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        unordered_map<int, int> m;
        m[0]++;
        
        int total = 0;
        helper(root, 0, sum, total, m);
        return total;
    }
    
    void helper(TreeNode *p, int cur, int sum, int &total, unordered_map<int, int> &m) {
        if (!p) return;
        
        cur += p->val;
        if (m.find(cur - sum) != m.end()) total += m[cur - sum];
        m[cur]++;
        
        helper(p->left, cur, sum, total, m);
        helper(p->right, cur, sum, total, m);
        
        m[cur]--;
    }
};



// class Solution {
// public:
//     void dfs(TreeNode* root, int target, int presum, int sum, int &res){
//         if(!root)return;
//         presum += root->val;
//         if (presum == sum)
//             res++;
//         dfs(root->left,target,presum,sum,res);
//         dfs(root->right,target,presum,sum,res);
//         return;
//         }
        
        
//     int pathSum(TreeNode* root, int sum) {
//         if(!root)return 0;
//         int res = 0;
//         dfs(root,sum,0,sum,res);
//         res += pathSum(root->left, sum);
//         res += pathSum(root->right, sum);
//         return res;
        
//     }
// };