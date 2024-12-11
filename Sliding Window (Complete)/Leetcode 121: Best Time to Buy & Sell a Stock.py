class Solution:
    '''
    You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
    You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
    Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
        Example 1:
        Input: prices = [10,1,5,6,7,1]
        Output: 6
    '''
    def maxProfit(self, prices):
        # We will use two pointers and sliding window to calculate equity purchase and liquidation
        # Remember, left is buy and right is well. Left will start at 0 and right + 1. maxP is max profit
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # Is the equity profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                #if we found the lowest price: l < r; We need to update l to r and increment r.
                l = r
            r += 1
        return maxP


sol = Solution()

prices1 = [10, 1, 5, 6, 7, 1]  # output: 6
prices2 = [10, 8, 7, 5, 2]  # output: 0

print(sol.maxProfit(prices1))
print(sol.maxProfit(prices2))
