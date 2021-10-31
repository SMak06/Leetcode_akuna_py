class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        count = 0
        curr = 0
        prod = 1
        sub = 0
        for i in range(len(nums)):
            prod = prod * nums[i]
            sub += 1 #this here adds the new number to sub count but not the actual count
            
            while prod >= k and curr <= i:  #the curr condition here is to check if the curr element is not greater than k as well as the prod
                prod = prod / nums[curr]
                curr += 1
                sub -= 1
                
            if prod < k:
                count += sub
        return count
        