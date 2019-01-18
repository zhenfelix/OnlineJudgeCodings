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
//     bool isPalindrome(ListNode* head) {
//         if(!head||!(head->next))return true;
//         ListNode *fast=head->next, *slow=head, *rev=NULL;
//         while(fast&&fast->next){
//             fast=fast->next->next;
//             ListNode *next=slow->next;
//             slow->next=rev;
//             rev=slow;
//             slow=next;
//         }
//         if(fast){
//             ListNode *next=slow->next;
//             slow->next=rev;
//             rev=slow;
//             slow=next;
//         }
//         else slow=slow->next;
//         while(rev){
//             if(rev->val!=slow->val)return false;
//             rev=rev->next;slow=slow->next;
//         }
//         return true;
//     }
// };

// int t = []{ std::cin.tie(nullptr); std::ios_base::sync_with_stdio(false); return 0; }();


class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (!head) return true;
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = nullptr;
        while (fast && fast->next) {
            fast = fast->next->next;
            ListNode* next = slow->next;
            // if (slow->next)
                slow->next = prev;
            prev = slow;
            slow = next;
        }
        if (fast)
            slow = slow->next;
        while (prev != nullptr && slow != nullptr) {
            if (prev->val != slow->val) return false;
            prev = prev->next;
            slow = slow->next;
        }
        return true;
    }
};