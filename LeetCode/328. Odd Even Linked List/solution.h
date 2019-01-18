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
//     ListNode* oddEvenList(ListNode* head) {
//         if(head==NULL||head->next==NULL)return head;
//         ListNode *odd=head, *even=head->next, *p=head->next->next;
//         bool flag=true;
//         while(p!=NULL){
//             ListNode *next=p->next;
//             if(flag){
//                 ListNode *tmp=odd->next;
//                 odd->next=p;
//                 p->next=tmp;
//                 odd=p;
//                 even->next=next;
//                 even=next;
                
//             }
//             flag=!flag;
//             p=next;
//         }
//         return head;
//     }
// };


class Solution {
public:
    ListNode* oddEvenList(ListNode* head) 
    {
        if(!head) return head;
        ListNode *odd=head, *evenhead=head->next, *even = evenhead;
        while(even && even->next)
        {
            odd->next = odd->next->next;
            even->next = even->next->next;
            odd = odd->next;
            even = even->next;
        }
        odd->next = evenhead;
        return head;
    }
};