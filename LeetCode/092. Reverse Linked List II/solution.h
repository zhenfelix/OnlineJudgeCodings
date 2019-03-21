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