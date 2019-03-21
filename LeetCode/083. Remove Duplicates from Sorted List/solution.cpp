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
//         if(head->next->val==head->val){
//             head->next=head->next->next;
//             return deleteDuplicates(head);
//         }
//         else{
//             head->next=deleteDuplicates(head->next);
//             return head;
//         }
//     }
// };

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==nullptr || head->next==nullptr)return head;
        head->next=deleteDuplicates(head->next);
        return head->val==head->next->val?head->next:head;
    }
};