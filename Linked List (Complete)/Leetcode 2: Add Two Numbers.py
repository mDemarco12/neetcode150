from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # this formats the output of our Linked List
    def __str__(self):
        # Create string representation
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return "->".join(values) + "->None"


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node
        dummy = ListNode()
        # create current node
        cur = dummy
        # create carry value
        carry = 0

        # if l1, l2, or carry are not null...
        while l1 or l2 or carry:
            # get the digits from list
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # add them together
            val = v1 + v2 + carry

            # get the carry
            carry = val // 10
            val = val % 10  # this gives us the 1's place in 15.
            cur.next = ListNode(val)

            # update the pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # return
        return dummy.next

    def create_linked_list(self, arr):

        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def sol(self) -> None:
        # create link lists
        l1 = self.create_linked_list([1, 2, 3])
        l2= self.create_linked_list([4, 5, 6])

        l3 = self.create_linked_list([9])
        l4 = self.create_linked_list([9])

        # print the linked lists
        print(self.addTwoNumbers(l1, l2))
        print(self.addTwoNumbers(l3, l4))


solution = Solution()

solution.sol()
