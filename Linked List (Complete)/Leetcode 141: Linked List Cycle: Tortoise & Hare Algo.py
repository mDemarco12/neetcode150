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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # in order to use Tortoise and Hare Algo, we need a slow and fast pointer...
        slow, fast = head, head

        # while fast and fast.next are not null...
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # check for cycle
            if slow == fast:
                return True
        return False

    # function for linked list
    def create_linked_list(self, arr):

        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # function to create the cycle
    def create_cycle(self, head, pos):
        if pos < 0:
            return head

        # Find node to connect to
        target = head
        for _ in range(pos):
            target = target.next

        # Find last node
        current = head
        while current.next:
            current = current.next

        # Create cycle
        current.next = target
        return head

    def sol(self) -> None:
        list1 = [1, 2, 3, 4]
        index1 = 1

        list2 = [1, 2]
        index2 = -1

        head1 = self.create_linked_list(list1)
        head2 = self.create_linked_list(list2)

        head1 = self.create_cycle(head1, index1)
        head2 = self.create_cycle(head2, index2)

        print(self.hasCycle(head1))  # True
        print(self.hasCycle(head2))  # False


solution = Solution()

solution.sol()
