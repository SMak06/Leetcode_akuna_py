class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums) #max could be the biggest element in the array
        minimum, maximum = 1, 1
        
        for n in nums:
            tempMax = n * maximum #to store the value of maximum before computing the new maximum
            maximum = max(n * maximum, n * minimum, n) #computes the max value
            minimum = min(tempMax, n * minimum, n) #keeps track of computed min value
            ans = max(ans,maximum)
        return ans
            