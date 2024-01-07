class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        if not A:
            return 0
        
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            index = 0
            
            while index < len(heights):
                if not stack or heights[index] >= heights[stack[-1]]:
                    stack.append(index)
                    index += 1
                else:
                    top = stack.pop()
                    width = index if not stack else index - stack[-1] - 1
                    max_area = max(max_area, heights[top] * width)
            
            while stack:
                top = stack.pop()
                width = index if not stack else len(heights) - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)
            
            return max_area
        
        rows, cols = len(A), len(A[0])
        heights, max_area = [0] * cols, 0
        
        for row in range(rows):
            for col in range(cols):
                heights[col] = heights[col] + 1 if A[row][col] == 1 else 0
            
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area
