from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def creat_link_list(a_list: List[int]) -> ListNode:
    node = ListNode(0)
    head = node
    for num in a_list:
        node.next = ListNode(num)
        node = node.next
    return head.next



class Solution:
    def add_two_number(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        """
        node = ListNode(0)
        head = node
        label = 0
        while l1 or l2:
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            value += label
            label = int(value / 10)
            value = value % 10
            node.next = ListNode(value)
            node = node.next
        if label > 0:
            node.next = ListNode(label)
        return head.next


if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]
    # l1 = [5]
    # l2 = [5]
    l1 = creat_link_list(l1)
    l2 = creat_link_list(l2)
    solution = Solution()
    l3 = solution.add_two_number(l1, l2)
    while l3:
        print(l3.val)
        l3 = l3.next

