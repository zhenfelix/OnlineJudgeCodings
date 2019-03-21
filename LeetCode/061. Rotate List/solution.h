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
//     ListNode* rotateRight(ListNode* head, int k) {
//         ListNode *dummy=new ListNode(0);
//         dummy->next=head;
//         ListNode *p=head;
//         ListNode *tail=nullptr;
//         int len=0;
//         while(p){
//             len++;
//             tail=p;
//             p=p->next;
//         }
//         if(len==0 || (k%len)==0)return head;
//         k%=len;
        
//         k=len-k;
//         p=dummy;
//         while(k--){
//             p=p->next;
//         }
//         dummy->next=p->next;
//         tail->next=head;
//         p->next=nullptr;
//         return dummy->next;
//     }
// };

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head) return head;
        
        int len=1; // number of nodes
        ListNode *newH, *tail;
        newH=tail=head;
        
        while(tail->next)  // get the number of nodes in the list
        {
            tail = tail->next;
            len++;
        }
        tail->next = head; // circle the link

        if(k %= len) 
        {
            for(auto i=0; i<len-k; i++) tail = tail->next; // the tail node is the (len-k)-th node (1st node is head)
        }
        newH = tail->next; 
        tail->next = NULL;
        return newH;
    }
};