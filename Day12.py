#Question: Best Time to Buy and Sell Stocks III
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        n = len(A)
        if n <= 1:
            return 0

        # Initialize the variables to keep track of the maximum profits
        profit1 = [0] * n
        profit2 = [0] * n

        # Forward pass: Calculate the maximum profit with one transaction
        min_price = A[0]
        for i in range(1, n):
            min_price = min(min_price, A[i])
            profit1[i] = max(profit1[i - 1], A[i] - min_price)

        # Backward pass: Calculate the maximum profit with two transactions
        max_price = A[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, A[i])
            profit2[i] = max(profit2[i + 1], max_price - A[i])

        # Calculate the maximum overall profit by combining the two transactions
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, profit1[i] + profit2[i])

        return max_profit