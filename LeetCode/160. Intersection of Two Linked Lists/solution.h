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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int a=0,b=0;
        ListNode *p;
        p=headA;
        while(p!=NULL){
            a++;
            p=p->next;
        }
        p=headB;
        while(p!=NULL){
            b++;
            p=p->next;
        }
        int delta=a>b?a-b:b-a;
        p=a>b?headA:headB;
        ListNode *q=a>b?headB:headA;
        while(delta--)p=p->next;
        while(p!=NULL&&p!=q){
            p=p->next;q=q->next;
        }
        return p;
    }
};