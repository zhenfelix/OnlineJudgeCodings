//Binary indexed tree
class Solution {
public:
    int lowbit(int x){return (x&(-x));}
    int getSum(int x, vector<int> &hash){
        int sums=0;
        while(x>0){
            sums+=hash[x];
            x-=lowbit(x);
        }
        return sums;
    }
    void update(int x, vector<int> &hash){
        int n=hash.size()-1;
        while(x<=n){
            hash[x]+=1;
            x+=lowbit(x);
        }
        return;
    }
    vector<int> countSmaller(vector<int>& nums) {
        int n=nums.size();
        vector<int> tmp=nums;
        vector<int> hash(n+1,0);
        vector<int> ans(n,0);
        unordered_map<int,int> mp;
        sort(tmp.begin(),tmp.end());
        for(int i=0;i<n;i++){
            if(i==0||tmp[i]!=tmp[i-1])mp[tmp[i]]=i+1;
            else continue;
        }
        for(int i=n-1;i>=0;i--){
            update(mp[nums[i]],hash);
            ans[i]=getSum(mp[nums[i]]-1,hash);
        }
        return ans;
    }
};


// Binary search tree
// struct Node 
// { 
//     int key; 
//     int numSmaller; // number of smaller values than the key in the sub-tree taking this node as root
//     Node *left, *right; 
    
//     Node() : left(0), right(0), numSmaller(0) {}
// }; 

// void insert(Node *node, int val, int &countSmaller) {

//     if (val < node->key) {
//         if (node->left == NULL) {
//             node->left = new Node;
//             node->left->key = val;
//         } else {
//             insert(node->left, val, countSmaller);
//         }
//         node->numSmaller += 1;      // there is one more value smaller than this node in its sub-tree
//     } else {
//         // count here
//         if (node->key == val) 
//             countSmaller += node->numSmaller;
//         else 
//             countSmaller += 1 + node->numSmaller;
            
//         if (node->right == NULL) {
//             node->right = new Node;
//             node->right->key = val;
//         } else {
//             insert(node->right, val, countSmaller);
//         }
//     }

// }

// class Solution {
// public:
//     vector<int> countSmaller(vector<int>& nums) {
//         if (nums.size() == 0) return vector<int>();
        
//         vector<int> count(nums.size());
//         for (int i = 0; i < (int)nums.size(); ++i) count[i] = 0;
//         if (nums.size() == 1) return count;
        
//         root = new Node;
//         root->key = nums[(int)nums.size()-1];        
//         for (int i = (int)nums.size() - 2; i >= 0; --i) {
//             insert(root, nums[i], count[i]);
//         }
        
//         return count;
//     }
    
//     Node *root;
// };