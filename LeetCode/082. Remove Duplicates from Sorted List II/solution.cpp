/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// class Solution {
// public:
//     ListNode* deleteDuplicates(ListNode* head) {
//         if(head==nullptr || head->next==nullptr)return head;
//         ListNode *next=head->next;
//         while(next!=nullptr && next->val==head->val)next=next->next;
//         if(next!=head->next){
//             return deleteDuplicates(next);
//         }
//         else{
//             head->next=deleteDuplicates(next);
//             return head;
//         }
//     }
// };


class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return 0;
        if (!head->next) return head;
        
        int val = head->val;
        ListNode* p = head->next;
        
        if (p->val != val) {
            head->next = deleteDuplicates(p);
            return head;
        } else {
            while (p && p->val == val) p = p->next;
            return deleteDuplicates(p);
        }
    }
};