//给定一个单向链表中的某个节点，请删除这个节点，但要求只能访问该节点。若该节点为尾节点，返回false，否则返回true
import java.util.*;

/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Remove {
    public boolean removeNode(ListNode pNode) {
        // write code here
        // if(pNode.next == null){
        //     pNode = null;
        //     return false;
        // }
        // else{
        //     pNode = null;
        //     return true;
        // }
        // 会错意，题目的意思不是这个
        if (pNode.next == null){
            return false;
        }
        
        pNode.val = pNode.next.val;
        pNode.next = pNode.next.next;
        return true;
    }
}