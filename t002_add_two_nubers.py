from lib_singly_nodelist import ListNode, create_node_list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = l1.val + l2.val
        carry = 0
        if s > 9:
            head = ListNode(s-10)
            carry = 1
        else:
            head = ListNode(s)
        p = head
        p1 = l1.next
        p2 = l2.next
        while p1 != None and p2 != None:
            s = p1.val + p2.val + carry
            if s > 9:
                p.next = ListNode(s-10)
                carry = 1
            else:
                p.next = ListNode(s)
                carry = 0
            p1, p2, p = p1.next, p2.next, p.next
        rest_p = p1 if p1 else p2
        while rest_p != None:
            if carry == 0:
                p.next == rest_p
                break
            else:
                s = rest_p.val + carry
                if s > 9:
                    p.next = ListNode(s-10)
                    carry = 1
                else:
                    p.next = ListNode(s)
                    carry = 0
            p, rest_p = p.next, rest_p.next
        if carry == 1:
            p.next = ListNode(1)
        return head
            
def test_args():
    s = Solution()
    func = s.addTwoNumbers
    test_cases = (
        ((create_node_list([2, 4, 3]), create_node_list([5, 6, 4])), create_node_list([7, 0, 8])),
        ((create_node_list([9, 9, 9, 9, 9, 9, 9]), create_node_list([9,9,9,9])), create_node_list([8,9,9,9,0,0,0,1])),
        ((create_node_list([0]), create_node_list([0])), create_node_list([0])),
        ((create_node_list([5]), create_node_list([5])), create_node_list([0, 1])),
        ((create_node_list([2,4,9]), create_node_list([5,6,4,9])), create_node_list([7,0,4,0,1])),

    )

    return func, test_cases