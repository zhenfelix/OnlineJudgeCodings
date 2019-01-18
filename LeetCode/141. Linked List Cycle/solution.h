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
    bool hasCycle(ListNode *head) {
        ListNode *a,*b;
        if(head==NULL)return false;
        if(head->next==NULL)return false;
        if(head->next->next==NULL)return false;
        a=head;b=head;
        while(1){
            a=a->next;
            b=b->next->next;
            if(a==b)return true;
            if(b==NULL)return false;
            if(b->next==NULL)return false;
        }
    }
};