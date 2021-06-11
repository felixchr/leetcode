# Definition for singly-linked list.
from lib_singly_nodelist import ListNode, create_node_list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode()
        ptr = new_head
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            if s > 9:
                carry = 1
                ptr.val = s - 10
            else:
                carry = 0
                ptr.val = s
            if carry == 1 or l1.next or l2.next:
                ptr.next = ListNode()
                ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        if l1 is None and l2 is None:
            if carry == 1:
                ptr.val = 1
        else:
            tmp_l = l1 if l1 else l2
            while tmp_l:
                print(tmp_l.val, carry)
                s = carry + tmp_l.val
                if s > 9:
                    carry = 1
                    ptr.val = s - 10
                else:
                    carry = 0
                    ptr.val = s
                if tmp_l.next:
                    tmp_l = tmp_l.next
                    ptr.next = ListNode()
                    ptr = ptr.next
                else:
                    if carry == 1:
                        ptr.next = ListNode(1)
                    break
        return new_head

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        s = ptr1.val + ptr2.val
        if s > 9:
            carry = 1
            s = s - 10
        new_head = ListNode(s)
        ptr = new_head
        while True:
            ptr1 = ptr1.next if ptr1 is not None else None
            ptr2 = ptr2.next if ptr2 is not None else None
            if ptr1 is None and ptr2 is None:
                break
            else:
                v1 = ptr1.val if ptr1 is not None else 0
                v2 = ptr2.val if ptr2 is not None else 0
            s = v1 + v2 + carry
            if s > 9:
                s, carry = s - 10, 1
            else:
                s, carry = s, 0
            ptr.next = ListNode(s)
            ptr = ptr.next
        if carry == 1:
            ptr.next = ListNode(1)
        return new_head


def test_args():
    s = Solution2()
    func = s.addTwoNumbers
    test_cases = (
        ((create_node_list([2, 4, 3]), create_node_list([5, 6, 4])), create_node_list([7, 0, 8])),
        ((create_node_list([9, 9, 9, 9, 9, 9, 9]), create_node_list([9,9,9,9])), create_node_list([8,9,9,9,0,0,0,1])),
        ((create_node_list([0]), create_node_list([0])), create_node_list([0])),
        ((create_node_list([5]), create_node_list([5])), create_node_list([0, 1])),
        ((create_node_list([2,4,9]), create_node_list([5,6,4,9])), create_node_list([7,0,4,0,1])),

    )

    return func, test_cases
