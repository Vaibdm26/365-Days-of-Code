class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # @param A : integer
    # @return a list of TreeNode
    def generateTrees(self, A):
        if A == 0:
            return []
        
        def generate_trees(start, end):
            if start > end:
                return [None]
            
            trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                trees.extend(TreeNode(i, l, r) for l in left_trees for r in right_trees)
            
            return trees
        return generate_trees(1, A)
