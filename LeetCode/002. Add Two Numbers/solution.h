// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode(int x) : val(x), next(NULL) {}
//  * };
//  */
// class Solution {
// public:
//     ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
//         ListNode* cur=l1, *late1, *late2=NULL;
//         int flag=0;
//         while(cur!=NULL&&l2!=NULL){
//             cur->val+=l2->val+flag;
//             flag=cur->val/10;
//             cur->val%=10;
//             late1=cur;
//             cur=cur->next;l2=l2->next;
//         }
//         while(cur!=NULL){
//             cur->val+=flag;
//             flag=cur->val/10;
//             cur->val%=10;
//             late2=cur;
//             cur=cur->next;
//         }
//         ListNode* L2=l2;
//         while(l2!=NULL){
//             l2->val+=flag;
//             flag=l2->val/10;
//             l2->val%=10;
//             late2=l2;
//             l2=l2->next;
//         }
//         if(L2!=NULL)late1->next=L2;
//         if(late2==NULL)late2=late1;
//         if(flag>0)late2->next=new ListNode(1);
//         return l1;
//     }
// };

class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode preHead(0), *p = &preHead;
    int extra = 0;
    while (l1 || l2 || extra) {
        int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + extra;
        extra = sum / 10;
        p->next = new ListNode(sum % 10);
        p = p->next;
        l1 = l1 ? l1->next : l1;
        l2 = l2 ? l2->next : l2;
    }
    return preHead.next;
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode();
        ListNode *head = dummy;
        int inc = 0;
        while (l1 || l2){
            if (l1) inc += l1->val, l1 = l1->next;
            if (l2) inc += l2->val, l2 = l2->next;
            head->next = new ListNode(inc%10);
            head = head->next;
            inc /= 10;
        }
        if (inc) head->next = new ListNode(inc%10);
        return dummy->next;
    }
};