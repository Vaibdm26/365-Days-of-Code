#Question: Min Jumps Array
class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)

        # If the array has only one element or is empty, no jump is needed
        if n <= 1:
            return 0

        # Initialize variables to keep track of the current reachable position, the maximum reachable position,
        # and the number of jumps
        curr_reach = 0
        max_reach = 0
        jumps = 0

        # Iterate through the array
        for i in range(n - 1):
            # Update the maximum reachable position
            max_reach = max(max_reach, i + A[i])

            # If the current position is equal to the current reachable position,
            # update the reachable position to the maximum reachable position and increment the jumps
            if i == curr_reach:
                curr_reach = max_reach
                jumps += 1

        # If the last index is reachable, return the number of jumps; otherwise, return -1
        return jumps if curr_reach >= n - 1 else -1
