/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int n=0;
        ListNode *head=root;
        vector<ListNode*> ans;
        while(head){
            head=head->next;
            n++;
        }
        int nums=n/k;
        int r=n%k;
        head=root;
        while(k--){
            ans.push_back(head);
            ListNode *pre=nullptr;
            for(int i=0;i<nums;i++){
                pre=head;
                head=head->next;
            }
            
            if(r>0){
                pre=head;
                head=head->next;
                r--;
            }
            if(pre)pre->next=nullptr;
        }
        // ListNode *p=new ListNode(n);
        // ans.push_back(p);
        return ans;
    }
};