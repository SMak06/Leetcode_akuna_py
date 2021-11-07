class MedianFinder:

    def __init__(self):
        self.lo, self.hi = [],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num) #we always push the new element to the lo heap
        heapq.heappush(self.hi, -heappop(self.lo)) #we pop the largest from the lo and push it to the hi
        if (len(self.lo) < len(self.hi)): #inside the loop itself we check if the length of hi becomes greater than self, if so, we pop from hi and push is back to lo to maintain our condition of the length of lo being atmost 1 greater than hi but not vise versa
            heapq.heappush(self.lo, -heappop(self.hi))
            
        
    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi): #if case is where len of lo is more than len of hi
            return -self.lo[0]
        else:
            return (-self.lo[0]+self.hi[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()