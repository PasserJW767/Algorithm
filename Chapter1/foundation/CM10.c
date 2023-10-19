//给定一个单向链表中的某个节点，请删除这个节点，但要求只能访问该节点。若该节点为尾节点，返回false，否则返回true
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