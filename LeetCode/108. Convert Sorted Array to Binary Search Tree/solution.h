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

// class Solution {
//     TreeNode* sortedArrayToBST(vector<int>& nums, int start, int end){
//         if(end<start) return NULL;
//         int midIdx=(end+start)/2;
//         TreeNode* root=new TreeNode(nums[midIdx]);
//         root->left=sortedArrayToBST(nums, start, midIdx-1);
//         root->right=sortedArrayToBST(nums, midIdx+1,end);
//         return root;
//     }
// public:
//     TreeNode* sortedArrayToBST(vector<int>& nums) {
//         return sortedArrayToBST(nums, 0,nums.size()-1);
//     }
// };

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if(nums.empty()) return nullptr; 
        //if(nums.size()==1) return new TreeNode(nums[0]); 
        
        size_t mid = nums.size()/2; 
        TreeNode* root = new TreeNode(nums[mid]); 
        
        vector<int> vecl(nums.begin(), nums.begin()+mid);        
        vector<int> vecr(nums.begin()+mid+1, nums.end()); 
        
        root->left = sortedArrayToBST(vecl); 
        root->right = sortedArrayToBST(vecr); 
        
        return root; 
    }
};