from typing_extensions import Optional


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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node, to prevent edge case
        dummy = ListNode()
        tail = dummy

        # iterate through each list
        while list1 and list2:
            # compare list1 to list2
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:  # update list2
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # if list1 is not null... next node of tail is list1
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # return
        return dummy.next

    # helper method for linked list
    def create_linked_list(self, arr):

        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # solution
    def sol(self):
        list1 = self.create_linked_list([1, 2, 4])
        list2 = self.create_linked_list([1, 3, 5])

        merged = self.mergeTwoLists(list1, list2)

        print("Merged list:", merged)


solution = Solution()

print(solution.sol())
