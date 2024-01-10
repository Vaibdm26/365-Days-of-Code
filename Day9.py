#Question : Max Product Subarray
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProduct(self, A):
        # Function definition: maxProduct(nums)
        def maxProduct(nums):
            if not nums:
                return 0

            max_product = nums[0]
            min_product = nums[0]
            result = nums[0]

            for i in range(1, len(nums)):
                if nums[i] < 0:
                    max_product, min_product = min_product, max_product

                max_product = max(nums[i], max_product * nums[i])
                min_product = min(nums[i], min_product * nums[i])

                result = max(result, max_product)

            return result
        
        # Call the function maxProduct(nums) with the input A
        return maxProduct(A)
