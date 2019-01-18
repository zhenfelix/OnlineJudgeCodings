#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


// class Solution {
// public:
//     ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
//         ListNode *head,*p;
//         head= new ListNode(0);
//         p=head;
//         while(l1!=NULL||l2!=NULL){
//             if(l2==NULL||(l1!=NULL&&l1->val<l2->val)){
//                 p->next=new ListNode(l1->val);
//                 l1=l1->next;
//             }
//             else{
//                 p->next=new ListNode(l2->val);
//                 l2=l2->next;
//             }
//             p=p->next;
//         }
//         return head->next;
//     }
// };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL)return l2;
        else if(l2==NULL)return l1;
        if(l1->val<=l2->val){
            l1->next=mergeTwoLists(l1->next,l2);
            return l1;
        }
        else{
            l2->next=mergeTwoLists(l1,l2->next);
            return l2;
        }
    }
};

// class Solution {
// public:
//     ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
//         ListNode dummy(INT_MIN);
//         ListNode *tail = &dummy;
        
//         while (l1 && l2) {
//             if (l1->val < l2->val) {
//                 tail->next = l1;
//                 l1 = l1->next;
//             } else {
//                 tail->next = l2;
//                 l2 = l2->next;
//             }
//             tail = tail->next;
//         }

//         tail->next = l1 ? l1 : l2;
//         return dummy.next;
//     }
// };
