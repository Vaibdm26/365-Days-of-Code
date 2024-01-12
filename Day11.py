#Question : Best Time to Buy and Sell Stocks II
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxProfit(self, A):
        n = len(A)
        if n <= 1:
            return 0
        
        max_profit = 0
        
        for i in range(1, n):
            if A[i] > A[i - 1]:
                max_profit += A[i] - A[i - 1]
        
        return max_profit
