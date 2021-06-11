from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, o: object) -> bool:
        while True:
            if self and o:
                if self.val == o.val:
                    self = self.next
                    o = o.next
                else:
                    return False
            elif self or o:
                return False
            else:
                break
        return True
    
    def __repr__(self) -> str:
        ptr = self
        l = []
        while ptr:
            l.append(ptr.val)
            ptr = ptr.next
        return 'ListNode: [{}]'.format(','.join([str(i) for i in l]))


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr = head
        while ptr:
            if not ptr.next:
                break
            ptr2 = ptr.next
            if ptr.val == ptr2.val:
                if ptr2.next:
                    ptr.next = ptr2.next
                else:
                    ptr.next = None
                    break
            else:
                ptr = ptr.next
        return head

def create_node_list(l: list):
    new_l = [ ListNode(i) for i in l]
    head = new_l[0]
    for i in range(len(l) - 1):
        new_l[i].next = new_l[i+1]
    return head

def print_node_list(l: ListNode):
    while l:
        print(l.val, end=' ')
        l = l.next


def test_args():
    s = Solution()
    func = s.deleteDuplicates
    test_cases = (
        (create_node_list([1, 1, 2]), create_node_list([1, 2])),
        (create_node_list([1, 1, 1]), create_node_list([1])),
        (create_node_list([1, 1, 2, 3, 3]), create_node_list([1, 2, 3])),
    )
    return func, test_cases