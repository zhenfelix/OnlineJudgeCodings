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
//     ListNode* swapPairs(ListNode* head) {
//         if(head==nullptr || head->next==nullptr)return head;
//         ListNode *first=head;
//         ListNode *second=head->next;
//         ListNode *next=second->next;
//         first->next=swapPairs(next);
//         second->next=first;
//         return second;
//     }
// };

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
    
        ListNode* succeding = head->next;
        head->next = swapPairs(head->next->next);
        succeding->next = head;

        return succeding;
    }
};