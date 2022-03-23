class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, o: object) -> bool:
        ptr = self
        while True:
            if ptr is None and o is None:
                break
            elif ptr is None or o is None:
                return False
            else:
                if ptr.val != o.val:
                    return False
                else:
                    ptr, o = ptr.next, o.next
        return True

    def __repr__(self) -> str:
        l = []
        ptr = self
        while ptr:
            l.append(str(ptr.val))
            ptr = ptr.next
        return 'ListNode([{}])'.format(','.join(l))

def create_node_list(l: list) -> ListNode:
    if len(l) == 0:
        return None
    node_arr = [ListNode(i) for i in l]
    head = node_arr[0]
    for i, node in enumerate(node_arr[:-1]):
        node.next = node_arr[i+1]
    return head

cnl = create_node_list