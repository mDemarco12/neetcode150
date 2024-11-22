class Solution:

    def __init__(self):
        # init the hashmap: Key : List of [value, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # edge case: Could supplement this section using a defaultdict*
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # init the result
        res = ""
        values = self.store.get(key, [])

        # binary search portion
        l, r = 0, len(values) - 1
        while l <= r:
            # define the middle
            m = (l + r) // 2
            # if the mid-value is less than the timestamp...
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

    def output(self) -> None:
        results = []
        input1 = ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1],
                  "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
        for i in range(len(input1)):
            if input1[i] == "TimeMap":
                continue
            elif input1[i] == "set":
                key, value, timestamp = input1[i + 1]
                self.set(key, value, timestamp)
            elif input1[i] == "get":
                key, timestamp = input1[i + 1]
                result = self.get(key, timestamp)
                results.append(result)
        print(results)


solution = Solution()

print(solution.output()) # output: happy, happy, sad
