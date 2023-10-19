/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};*/
#include <cstddef>
class Remove {
public:
    bool removeNode(ListNode* pNode) {
        // My Code
        // if(pNode->next == NULL){
        //     pNode = NULL;
        //     return false;
        // }
        // else{
        //     pNode = NULL;
        //     return true;
        // }
        // write code here
        // 题目的意思是，该节点是尾节点返回false，如果非尾节点则将该节点在单链表上断开
        if(pNode->next == NULL){
            return false;
        }
        
        pNode->val = pNode->next->val;
        pNode->next = pNode->next->next;
        return true;
    }
};