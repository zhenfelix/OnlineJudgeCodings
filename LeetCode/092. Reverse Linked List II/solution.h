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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode *f, *cur = head, *pre, *nxt, *dummy = new ListNode();
        dummy->next = head;
        pre = dummy;
        for (int i = 1; i <= right; i++){
            nxt = cur->next;
            if (i == left) f = pre;
            if (i > left){
                cur->next = pre;
            }
            pre = cur;
            cur = nxt;
        }
        f->next->next = cur;
        f->next = pre;
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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        // if(m==n)return head;
        ListNode *H=new ListNode(0);
        ListNode *pre=H;
        pre->next=head;
        for(int i=1;i<m;i++){
            head=head->next;
            pre=pre->next;
            
        }
        ListNode *cut=pre;
        for(int i=m;i<=n;i++){
            ListNode *next=head->next;
            head->next=pre;
            pre=head;
            head=next;
        }
        ListNode *tail=cut->next;
        cut->next=pre;
        tail->next=head;
        return H->next;
         
    }
};