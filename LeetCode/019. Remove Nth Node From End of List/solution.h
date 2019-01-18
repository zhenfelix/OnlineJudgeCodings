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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *start=head,*last=head;
        while(n--)last=last->next;
        if(!last)return head->next;//equivalent list length = n
        while(last->next){
            start=start->next;
            last=last->next;
        }
        start->next=start->next->next;
        return head;
    }
};