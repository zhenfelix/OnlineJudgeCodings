#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
 
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
//     ListNode* reverseList(ListNode* head) {
//         if(head==NULL||head->next==NULL)return head;
//         ListNode* H=reverseList(head->next);
//         ListNode* p=head;
//         while(p->next!=NULL)p=p->next;
//         p->next=head;
//         p->next->next=NULL;
//         return H;
//     }
// };

// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
//         if (!head || !(head -> next)) {
//             return head;
//         }
//         ListNode* node = reverseList(head -> next);
//         head -> next -> next = head;
//         head -> next = NULL;
//         return node;
//     }
// };

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = NULL;
        while (head) {
            ListNode* next = head -> next;
            head -> next = pre;
            pre = head;
            head = next;
        }
        return pre;
    }
};