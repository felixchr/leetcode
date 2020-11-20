# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        newL = None
        if l1.val < l2.val:
            newL = ListNode(l1.val)
            l1 = l1.next
        else:
            newL = ListNode(l2.val)
            l2 = l2.next
        tmpL = newL
        while l1 and l2:
            if l1.val < l2.val:
                tmpL.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmpL.next = ListNode(l2.val)
                l2 = l2.next
            tmpL = tmpL.next
        tmpL2 = l1 if l1 else l2
        while tmpL2:
            tmpL.next = ListNode(tmpL2.val)
            tmpL = tmpL.next
            tmpL2 = tmpL2.next
        return newL

def create_from_list(l):
    if not l:
        return None
    newL = ListNode(l[0])
    tmpL = newL
    for i in l[1:]:
        tmpL.next = ListNode(i)
        tmpL = tmpL.next
    return newL

def to_list(l):
    if not l:
        return []
    ret = []
    while l:
        ret.append(l.val)
        l = l.next
    return ret

def test_solution():
    s = Solution()
    test_cases = (
        ([-9, 3], [5, 7], [-9, 3, 5, 7]),
        ([], [], []),
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    )
    for list1, list2, list_ret in test_cases:
        print(list1, list2, list_ret)
        l1 = create_from_list(list1)
        l2 = create_from_list(list2)
        l_ret = to_list(s.mergeTwoLists(l1, l2))
        if l_ret != list_ret:
            print(l_ret)
            print('Failed!')
            break
    else:
        print('Passed!')