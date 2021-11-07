class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        original = n
        count = 0
        nums = []
        while(n):
            count+=1
            nums.append(n%10)
            n//=10
        nums.reverse()
        
        def fac2(n,k):
            return math.factorial(n)//math.factorial(n-k)
        
        numbers = 0
        for i in range(count-1):
            numbers += 9*(math.factorial(9)//math.factorial(9-i))
            
        already_visited_digits = set()
        for i,n in enumerate(nums):
            k = 0
            for j in range((1 if i==0 else 0), (n+1 if i==count-1 else n)):
                if(j in already_visited_digits):
                    continue
                k += 1
            numbers += k * fac2(10-i-1, count-i-1)
            if n in already_visited_digits:
                # All the numbers with this prefix will have at least one common digit
                break
            already_visited_digits.add(n)
                  
                       
        return original - numbers
