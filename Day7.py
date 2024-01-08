#Question : Distinct Subsequences
class Solution:
    def numDistinct(self, A, B):
        len_A, len_B = len(A), len(B)
        
        dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]
        
        for i in range(len_A + 1):
            dp[i][0] = 1  # Empty subsequence of B can be formed by deleting all characters of A
        
        for i in range(1, len_A + 1):
            for j in range(1, len_B + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[len_A][len_B]
