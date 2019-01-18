#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("Reverse LInked List", "ReverseLinkedList")
{
    Solution s;
    
    vector<int> v1{1,2,3};
    vector<int> v2{3,2,1};
    vector<int> ans;
    ListNode* head=new ListNode(0);
    ListNode* p=head;
    for(int i: v1){
        p->next=new ListNode(i);
        p=p->next;
    }
    head=head->next;
    ListNode* ansList = s.reverseList(head);
    while(ansList!=NULL){
        ans.push_back(ansList->val);
        ansList=ansList->next;
    }
    REQUIRE( (ans == v2) );
    
 
}

