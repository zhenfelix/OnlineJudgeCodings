/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
//     ListNode* findMid(ListNode* head){
//         ListNode *fast=head;
//         ListNode *pre=NULL;
//         ListNode *slow=head;
//         while(fast!=NULL && fast->next!=NULL){
//             pre=slow;
//             slow=slow->next;
//             fast=fast->next->next;
//         }
//         if(pre!=NULL)pre->next=NULL;
//         return slow;
//     }
//     TreeNode* sortedListToBST(ListNode* head) {
//         if(head==NULL)return NULL;
//         ListNode *mid=findMid(head);
//         TreeNode* root=new TreeNode(mid->val);
//         if(head==mid)return root;
//         root->left=sortedListToBST(head);
//         root->right=sortedListToBST(mid->next);
//         return root;
//     }
// };


class Solution{
public:
    vector<int> arr;
    TreeNode* helper(int left, int right){
        if(left>right)return NULL;
        int mid=(left+right)/2;
        TreeNode* root=new TreeNode(arr[mid]);
        if(left==right)return root;
        root->left=helper(left,mid-1);
        root->right=helper(mid+1,right);
        return root;
    }
    TreeNode* sortedListToBST(ListNode* head){
        while(head!=NULL){
            arr.push_back(head->val);
            head=head->next;
        }
        return helper(0,arr.size()-1);
    }
};