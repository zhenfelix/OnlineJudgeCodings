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
    ListNode* helper(ListNode *head, ListNode* target, bool even){
        if(even && head->next==target){
            ListNode *ans=head->next->next;
            head->next->next=nullptr;
            return ans;
        }
        if(!even && head==target){
            ListNode *ans=head->next;
            head->next=nullptr;
            return ans;
        }
        ListNode *next=helper(head->next, target, even);
        ListNode *ans=next->next;
        next->next=head->next;
        head->next=next;
        return ans;
    }
    void reorderList(ListNode* head) {
        ListNode *fast=head, *slow=head;
        if(head==nullptr)return;
        while(fast!=nullptr && fast->next!=nullptr){
            slow=slow->next;
            fast=fast->next->next;
        }
        if(fast==nullptr)helper(head, slow, true);
        else helper(head, slow, false);
    }
};

// ListNode * reorderList(ListNode *head, int len){
//     if(len == 0)
//         return NULL;
//     if( len == 1 )
//         return head;
//     if( len == 2 )
//         return head->next;
//     ListNode * tail = reorderList(head->next, len-2);
//     ListNode * tmp = tail->next;
//     tail->next = tail->next->next;
//     tmp->next = head->next;
//     head->next = tmp;
//     return tail;
// }

// void reorderList(ListNode *head) {  //recursive
//     ListNode  * tail = NULL;
//     tail = reorderList(head, getLength(head));
// }