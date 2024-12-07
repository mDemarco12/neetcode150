class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        # left - LRU : right- most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev  # node is no longer between prev and next

    # insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # take the node, remove it from list, then reinsert at the right most pos
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val  # This tell's use the node and val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # before we insert, remove from list
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        # insert node into doubly linked list
        self.insert(self.cache[key])

        # does the length of cache exceed cap?
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def test_operations(self):
        input1 = ["LRUCache", [2], "put", [1, 10], "get", [1],
                  "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

        # Initialize result list
        result = [None]  # First operation is constructor

        # Process each operation
        i = 1
        while i < len(input1):
            operation = input1[i]

            if operation == "put":
                key, value = input1[i + 1]
                self.put(key, value)
                result.append(None)
                i += 2
            elif operation == "get":
                key = input1[i + 1][0]
                result.append(self.get(key))
                i += 2
            else:
                i += 1

        return result


def main():
    # Create cache with capacity 2 and run tests
    lru = LRUCache(2)
    results = lru.test_operations()
    print("Results:", results)
    # Expected output: [None, None, 10, None, None, 20, -1]
    return results


if __name__ == "__main__":
    main()
