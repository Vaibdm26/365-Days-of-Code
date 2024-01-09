#Question : Unique Paths in a Grid
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        if not A or A[0][0] == 1:
            return 0

        rows, cols = len(A), len(A[0])

        # Initialize a 2D array to store the number of unique paths
        dp = [[0] * cols for _ in range(rows)]

        # Set the starting point to 1
        dp[0][0] = 1 if A[0][0] == 0 else 0

        # Fill the first row and first column
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] if A[i][0] == 0 else 0

        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] if A[0][j] == 0 else 0

        # Fill the rest of the grid
        for i in range(1, rows):
            for j in range(1, cols):
                if A[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[rows - 1][cols - 1]