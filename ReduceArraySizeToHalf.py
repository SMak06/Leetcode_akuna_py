class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        #Here's what's happening
        #1.create a dict with the frequencies
        #2.create a list out of the values of the dict and sort it
        #3.take the last element(biggest) and add it to maxSum and remove it from the list
        #4.loop step 3. until maxSum is >= half the length of the given array
        #5.if majority of the frequency is 1, subtract maxSum from halfLength and add it to the existing count
        #6.return count which kept the count of the number of elements used
        
        

        elementCount = {} #define empty dict
        
        
        for element in arr:  #add the frequeny of the numbers into the dict
            if element in elementCount:
                elementCount[element] += 1  #increase frequency count if element is there in the dict
            else:
                elementCount[element] = 1  #else add the element to the dict
                
                
        maxSum, halfLength, count = 0, int(len(arr)/2), 0 #maxSum is supposed to be equal to halfLength in the end
        allValues = list(elementCount.values()) #create a list out of values in the dict
        allValues.sort() #sort the list
        
        while True:
            if(maxSum >= halfLength): break    #main condition to break out of the loop
            
            #case where there are a majority of 1s. If 1 is encountered all the other elements will be 1 since list is sorted. This is to cater to the edge case where frequency of majority/all of the elements is 1.
            if(allValues[-1] == 1):   
                count = count + (halfLength - maxSum)
                break
                
            maxSum += allValues[-1] 
            count +=1
            allValues.remove(allValues[-1]) #removing the biggest value from the sorted list

        return count

        #time complexity is O(nlogn)
        #space complexity is O(n)