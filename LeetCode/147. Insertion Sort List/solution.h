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
    ListNode* insertionSortList(ListNode* head) {
        ListNode *psudoHead=new ListNode(INT_MIN);
        ListNode *pre_head=psudoHead;
        pre_head->next=head;
        while(head){
            ListNode *next=head->next;
            ListNode *pre=psudoHead;
            ListNode *cur=psudoHead->next;
            while(cur!=head && cur->val<=head->val){
                pre=cur;
                cur=cur->next;
            }
            if(cur!=head){
                pre->next=head;
                head->next=cur;
                // while(cur->next!=head)cur=cur->next;
                // cur->next=next;
                pre_head->next=next;
            }
            else {pre_head=head;}
            head=next;
        }
        return psudoHead->next;
    }
};


// class Solution {
// public:
//     ListNode* insertionSortList(ListNode* head) {
//         ListNode* dummy = new ListNode(0);
//         dummy -> next = head;
//         ListNode *pre = dummy, *cur = head;
//         while (cur) {
//             if ((cur -> next) && (cur -> next -> val < cur -> val)) {
//                 while ((pre -> next) && (pre -> next -> val < cur -> next -> val)) {
//                     pre = pre -> next;
//                 }
//                 ListNode* temp = pre -> next;
//                 pre -> next = cur -> next;
//                 cur -> next = cur -> next -> next;
//                 pre -> next -> next = temp;
//                 pre = dummy;
//             }
//             else {
//                 cur = cur -> next;
//             }
//         }
//         return dummy -> next;
//     }
// };