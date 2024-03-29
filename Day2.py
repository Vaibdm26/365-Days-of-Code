#Question : Majority Element
class Solution:
    def majorityElement(self, A):
        if len(A) == 1:
            return A[0]
        
        counts = {}
        n = len(A)
        
        for num in A:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
            if counts[num] > n // 2:
                return num
        
        return -1  # Returning -1 if no majority element is found
