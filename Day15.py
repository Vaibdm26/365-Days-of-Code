#Question : Max Sum Path in Binary Tree
# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, A):
        # Helper function to calculate the maximum path sum at each node
        def maxPathSumHelper(node):
            nonlocal max_sum
            if not node:
                return 0

            # Calculate maximum path sum for left and right subtrees
            left_sum = max(0, maxPathSumHelper(node.left))
            right_sum = max(0, maxPathSumHelper(node.right))

            # Update the maximum path sum considering the current node
            max_sum = max(max_sum, left_sum + right_sum + node.val)

            # Return the maximum path sum including the current node
            return max(left_sum, right_sum) + node.val

        max_sum = float('-inf')  # Initialize with negative infinity
        maxPathSumHelper(A)  # Call the helper function to update max_sum
        return max_sum
