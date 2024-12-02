from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # declare variables
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # while n is greater than 0 and right is not null...
        while n > 0 and right:
            # we want to keep shifting right
            right = right.next
            n -= 1  # we decrement n by 1 because once we reach 0, we shifted by the target amount

        # keep shifting both pointers and keep going till right reaches null (end)
        while right:
            left = left.next
            right = right.next

            # delete the target node by updating the left pointer's next to the following index
        left.next = left.next.next
        return dummy.next  # this will return the entire Linked List

    # this creates the Linked List
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
        head1 = self.create_linked_list([1, 2, 3, 4, 5])
        head2 = self.create_linked_list([1, 2])
        n1 = 2
        n2 = 1

        print(self.removeNthFromEnd(head1, n1))
        print(self.removeNthFromEnd(head2, n2))

solution = Solution()

print(solution.sol())
