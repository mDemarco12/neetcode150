class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Example usage
solution = minStack()

val1 = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
val2 = ["MinStack", "push", -2, "push", 0, "push", -3, "getMin", "pop", "top", "getMin"]

for operation in val1:
    if operation == "MinStack":
        pass  # Ignore the "MinStack" operation
    elif operation == "push":
        solution.push(val1[val1.index(operation) + 1])
    elif operation == "pop":
        solution.pop()
    elif operation == "top":
        print(solution.top())
    elif operation == "getMin":
        print(solution.getMin())

print()

for operation in val2:
    if operation == "MinStack":
        pass  # Ignore the "MinStack" operation
    elif operation == "push":
        solution.push(val2[val2.index(operation) + 1])
    elif operation == "pop":
        solution.pop()
    elif operation == "top":
        print(solution.top())
    elif operation == "getMin":
        print(solution.getMin())