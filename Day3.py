Question : Distribute Candy
class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        candies = [1] * n  # Initialize candies for each child with 1
        
        # Traverse left to right to satisfy increasing ratings
        for i in range(1, n):
            if A[i] > A[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Traverse right to left to satisfy decreasing ratings
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
        
