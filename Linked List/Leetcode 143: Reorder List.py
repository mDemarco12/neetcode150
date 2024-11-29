from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # Create string representation
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return "->".join(values) + "->None"


class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        # declare vars to find the middle of the linked list
        slow, fast = head, head.next

        # while fast is not null and fast has not reached the end of the list...
        while fast and fast.next:
            slow = slow.next  # increment by 1
            fast = fast.next.next  # increment by 2

        # beginning of the 2nd half
        second = slow.next
        prev = slow.next = None

        # reverse the 2nd half of the list
        while second:
            temp = second.next  # temp will = next node
            second.next = prev
            prev = second  # the previous is saved
            second = temp  # second is incremented

        # merge the two half's
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        return head

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
        head1 = self.create_linked_list([2, 4, 6, 8])
        head2 = self.create_linked_list([2, 4, 6, 8, 10])

        # test to make sure linked list is working
        print("Linked List In-Order: ")
        print(head1)
        print(head2, "\n")

        # reorder
        reorder1 = self.reorderList(head1)
        reorder2 = self.reorderList(head2)

        # print
        print("Reordered Linked List: ")
        print(reorder1)
        print(reorder2)


solution = Solution()

print(solution.sol())
