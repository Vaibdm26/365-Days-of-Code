#Question: Regular Expression Match
class Solution:
    def isMatch(self, A, B):
        # Create a 2D dp array to store intermediate results
        dp = [[False] * (len(B) + 1) for _ in range(len(A) + 1)]
        
        # An empty pattern matches an empty string
        dp[0][0] = True
        
        # Fill in the dp array based on the pattern and string
        for i in range(1, len(B) + 1):
            if B[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]
        
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if B[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif B[j - 1] == '?' or A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return 1 if dp[len(A)][len(B)] else 0
