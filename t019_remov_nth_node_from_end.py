from typing import Optional
from lib_singly_nodelist import ListNode, create_node_list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        p = head
        while p != None:
            node_list.append(p)
            p = p.next
        length = len(node_list)
        if n == 1:
            if length == 1:
                return None
            else:
                node_list[-2].next = None
            node_list.pop(-1)
        elif n == length:
            head = head.next
        else:
            node_list[-n-1].next = node_list[-n+1]
        node_list.pop(-n)
        return head

def test_args():
    s = Solution()
    func = s.removeNthFromEnd
    test_cases = (
        ((create_node_list([1,2,3,4,5]), 2), create_node_list([1,2,3,5])),
        ((create_node_list([1]),1), None),
        ((create_node_list([1,2]),1), create_node_list([1])),
        ((create_node_list([1,2]),2), create_node_list([2])),
    )
    return func, test_cases