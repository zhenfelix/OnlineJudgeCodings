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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *dummy = new ListNode();
        ListNode *pre = dummy, *cur = head, *nxt, *f, *t;
        dummy->next = head;
        while(1){
            t = cur;
            for (int i = 0; i < k-1 && t; i++) t = t->next;
            if (!t)
                return dummy->next;
            t = t->next;
            f = pre;
            // cout << cur->val << " " << f->val << endl;
            for (int i = 0; i < k; i++){
                nxt = cur->next;
                cur->next = pre;
                pre = cur;
                cur = nxt;
            }
            f->next->next = t;
            swap(f->next,pre);
        }
        return nullptr;
    }

};




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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head)
            return head;
        // cout << head << " " << head->val  << endl;
        auto [h,t] = reverseK(head,k);
        if (!h)
            return head;
        // cout << head << " " << head->val << " " << h->val << endl;
        head->next = reverseKGroup(t,k);
        return h;
    }

    pair<ListNode*,ListNode*> reverseK(ListNode* head, int k){
        if (!head)
            return {nullptr, nullptr};
        if (k == 1)
            return {head, head->next};
        
        ListNode *nxt = head->next;
        auto [h,t] = reverseK(head->next,k-1);
        if (!h)
            return {h,t};
        nxt->next = head;
        return {h,t};
    }
};