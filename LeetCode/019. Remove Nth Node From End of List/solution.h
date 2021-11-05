/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy = new ListNode(), *slow, *fast;
        dummy->next = head;
        fast = slow = dummy;
        for (int i = 0; i < n; i++)
            fast = fast->next;
        while (fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return dummy->next;
    }
};


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