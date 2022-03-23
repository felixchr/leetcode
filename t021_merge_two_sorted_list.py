from typing import Optional
from lib_singly_nodelist import ListNode, create_node_list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        pointer = head
        
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        pointer.next = list1 if list1 else list2
        return head

def test_args():
    s = Solution()
    func = s.mergeTwoLists
    test_cases = (
        ((create_node_list([1,2,4]), create_node_list([1,3,4])), create_node_list([1,1,2,3,4,4])),
        ((create_node_list([]), create_node_list([])), create_node_list([])),
        ((create_node_list([]), create_node_list([0])), create_node_list([0])),
    )
    return func, test_cases

