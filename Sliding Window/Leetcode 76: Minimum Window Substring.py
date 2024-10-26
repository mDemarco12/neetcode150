class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge cases
        if t == "": return ""

        counT, window = {}, {}

        # init counT map. if c exists, get the count of c, else 0
        for c in t:
            counT[c] = 1 + counT.get(c, 0)
        # have will start @0, and need is equal to T
        have, need = 0, len(counT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        # for the right pointer in length s
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # is c is even a char in counT?
            if c in counT and window[c] == counT[c]:
                have += 1
            # does 'have' equal need?
            while have == need:
                # condition met, update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # shrink the window
                window[s[l]] -= 1
                # make sure 'have' is adjusted for shrinkage.
                if s[l] in counT and window[s[l]] < counT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""


solution = Solution()
s1, t1 = "ADOBECODEBANC", "ABC"
s2, t2 = "a", "a"

print(solution.minWindow(s1, t1))
print(solution.minWindow(s2, t2))
