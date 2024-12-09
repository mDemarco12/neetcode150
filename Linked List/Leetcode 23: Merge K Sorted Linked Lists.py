from typing import Optional, List


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # edge case...
        if not lists or len(lists) == 0:
            return None

        # take pairs of linked lists and merge them
        while len(lists) > 1:
            mergedList = []

            # iterate through each list, increment by 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeList(l1, l2))
            lists = mergedList
        return lists[0]

    # helper function
    def mergeList(self, l1, l2):
        # todo
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

    # function for individual linked lists
    def create_linked_list(self, lists):
        if not lists:
            return []

        result = []
        for arr in lists:
            if not arr:
                result.append(None)
                continue

            head = ListNode(arr[0])
            current = head
            for val in arr[1:]:
                current.next = ListNode(val)
                current = current.next
            result.append(head)

        return result

    # solution method
    def sol(self) -> None:
        lists = [[1, 2, 4], [1, 3, 5], [3, 6]]
        lists2 = [[]]

        l1 = self.create_linked_list(lists)
        l2 = self.create_linked_list(lists2)

        print(self.mergeKLists(l1))
        print(self.mergeKLists(l2))


solution = Solution()

solution.sol()
