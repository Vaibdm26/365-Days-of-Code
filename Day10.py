#Question : Ways to Decode
class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if not A or A[0] == '0':
            return 0

        mod = 10**9 + 7
        n = len(A)

        # Initialize an array to store the number of ways to decode at each position
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if A[0] != '0' else 0

        for i in range(2, n + 1):
            # Check if the current digit is not '0'
            if A[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check if the current and previous digits form a valid two-digit number
            two_digit = int(A[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] = (dp[i] + dp[i - 2]) % mod

        return dp[n] % mod

# Test case
solution = Solution()
print(solution.numDecodings("5163490394499093221199401898020270545859326357520618953580237168826696965537789565062429676962877038781708385575876312877941367557410101383684194057405018861234394660905712238428675120866930196204792703765204322329401298924190"))
