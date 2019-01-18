```c++
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {

        ListNode *res = new ListNode(0);
        ListNode *ptr = res;
        while(l1 && l2){
            if(l1->val <= l2->val){
                ptr->next = l1;
                l1 = l1->next;
            }else if(l2->val < l1->val){
                ptr->next = l2;
                l2 = l2->next;
            }
            ptr = ptr->next;
        }

        if(l1) ptr->next = l1;
        if(l2) ptr->next = l2;

        return res->next;

    }
};
```
