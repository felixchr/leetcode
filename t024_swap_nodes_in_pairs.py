from typing import Optional
from lib_singly_nodelist import ListNode, create_node_list

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        ptr1 = head
        head = ptr1.next
        ptr2 = head
        while ptr2 is not None:
            tmpPtr = ptr2.next
            ptr1.next = tmpPtr
            ptr2.next = ptr1
            if tmpPtr is None:
                break
            else:
                ptr1 = tmpPtr
                ptr2 = tmpPtr.next

        return head

def test_args():
    s = Solution()
    func = s.swapPairs
    test_cases = (
        ((create_node_list([1,2,3,4]),), create_node_list([2,1,4,3])),
        ((create_node_list([]),), create_node_list([])),
        ((create_node_list([1]),), create_node_list([1])),
    )
    return func, test_cases
        
