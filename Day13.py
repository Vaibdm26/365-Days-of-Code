#Question : Scramble String
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isScramble(self, A, B):
        # Base case: If the strings are equal, they are scrambled
        if A == B:
            return 1
        
        # If the characters in the strings don't match, they can't be scrambled
        if sorted(A) != sorted(B):
            return 0
        
        n = len(A)
        
        # Check all possible split points
        for i in range(1, n):
            # Check if the substrings are scrambled in both orders
            if (self.isScramble(A[:i], B[:i]) and self.isScramble(A[i:], B[i:])) or \
               (self.isScramble(A[:i], B[n-i:]) and self.isScramble(A[i:], B[:n-i])):
                return 1
        
        # If no valid split point is found, the strings are not scrambled
        return 0
